from AvitoAPI.Modules import Info, ShortTermRent
from threading import Thread
from time import sleep

import requests
import logging
import json

class Profile:
	"""
	Обработчик взаимодействий профиля с API Авито.
	"""
	
	#==========================================================================================#
	# >>>>> МОДУЛИ API <<<<< #
	#==========================================================================================#
	
	@property
	def info(self) -> Info:
		"""Модуль API: информация о пользователе."""
		
		return Info(self.__Profile, self.request)

	@property
	def short_term_rent(self) -> ShortTermRent:
		"""Модуль API: краткосрочная аренда."""
		
		return ShortTermRent(self.__Profile, self.request)

	#==========================================================================================#
	# >>>>> ПРИВАТНЫЕ МЕТОДЫ <<<<< #
	#==========================================================================================#
			
	def __UpdaterThread(self):
		"""
		Поток обновления токена доступа Авито (каждые 23 часа).
		"""
		
		# Постоянно.
		while True:
			# Выжидание 23-ёх часов.
			sleep(1380)
			# Обновление токен.
			self.refresh_access_token()
			
	def __SupervisorThread(self):
		"""
		Поток-надзиратель, перезапускающий обновление токена доступа в случае сбоя (каждые 5 минут).
		"""
		
		# Постоянно.
		while True:
			# Выжидание 5-ти минут.
			sleep(5 * 60)

			# Если поток обновления токена остановлен.
			if self.__Updater.is_alive() == False:
				# Запись в лог предупреждения: поток обновления токена был остановлен.
				if self.__Logging: logging.warning(f"Profile: {self.__ProfileID}. Token updater thread was stopped.")
				# Реинициализация потока обновления токена.
				self.__Updater = Thread(target = self.__UpdaterThread, name = f"Profile {self.__ProfileID} supervisor thred.")
				# Запуск потока.
				self.__Updater.start()
				
	#==========================================================================================#
	# >>>>> ПУБЛИЧНЫЕ МЕТОДЫ <<<<< #
	#==========================================================================================#
		
	def __init__(self, profile: int | str, client_id: str, client_secret: str, autorefresh: bool = True, use_supervisor: bool = False, logging: bool = False):
		"""
		Обработчик взаимодействий с API Авито.
			profile – номер профиля Авито;
			client_id – номер клиента API Авито;
			client_secret – секретный ключ API Авито;
			autorefresh – указывает, нужно ли обновлять токен доступа каждые 23 часа;
			use_supervisor – указывает, нужно ли запускать поток, следящий за непрерывной работой процесса обновления токена;
			logging – указывает, необходимо ли вести логи при помощи стандартного модуля Python.
		"""

		#---> Генерация динамических свойств.
		#==========================================================================================#
		# Сессия запросов.
		self.__Session = requests.Session()
		# Секретный ключ клиента.
		self.__ClientSecret = client_secret
		# Номер профиля Авито.
		self.__Profile = int(profile)
		# ID клиента.
		self.__ClientID = client_id
		#  Текущий токен.
		self.__AccessToken = None
		# Переключатель: нужно ли вести логи.
		self.__Logging = logging
		# Поток-надзиратель.
		self.__Supervisor = Thread(target = self.__SupervisorThread, name = f"Profile {profile} updater thred.")
		# Поток обновления токена.
		self.__Updater = Thread(target = self.__UpdaterThread, name = f"Profile {profile} supervisor thred.")
		
		# Получение токена доступа.
		self.refresh_access_token()
		
		# Если указано, запустить поток обновления токена доступа.
		if autorefresh == True: self.__Updater.start()
		# Если указано, запустить поток надзиратель.
		if autorefresh == True and use_supervisor == True : self.__Supervisor.start()
			
	def get_access_token(self, bearer: bool = True) -> str | None:
		"""
		Возвращает токен доступа API Авито.
			bearer – указывает, нужно ли добавлять к токену идентификатор типа.
		"""
		# Токен доступа.
		AccessToken = None
		
		# Если данные токена доступны.
		if self.__AccessToken != None:
			# Тип токена.
			TokenType = str()
			# Если указано, добавить идентификатор токена.
			if bearer == True: TokenType = self.__AccessToken["token_type"] + " "
			# Формирование токена.
			AccessToken = TokenType + self.__AccessToken["access_token"]

		return AccessToken
	
	def get(self, url: str, headers: dict | None = None, params: dict | None = None, json: dict | None = None) -> requests.Response:
		"""
		Отправляет GET-запрос с автоматической подстановкой токена доступа.
			url – адрес запроса;
			headers – заголовки запроса;
			params – параметры запроса;
			json – словарь для сериализации в JSON и отправки в качестве тела запроса.
		"""
		
		# Инициализация загловков.
		if headers == None: headers = dict()
		# Удаление заголовка авторизации в нижнем регистре.
		if "authorization" in headers.keys(): del headers["authorization"]
		# Подстановка токена.
		headers["Authorization"] = self.get_access_token()
		# Отправка GET-запроса.
		Response = self.__Session.get(url, headers = headers, params = params, json = json)
		
		return Response
	
	def post(self, url: str, headers: dict | None = None, params: dict | None = None, json: dict | None = None) -> requests.Response:
		"""
		Отправляет POST-запрос с автоматической подстановкой токена доступа.
			url – адрес запроса;
			headers – заголовки запроса;
			params – параметры запроса;
			json – словарь для сериализации в JSON и отправки в качестве тела запроса.
		"""
		
		# Инициализация загловков.
		if headers == None: headers = dict()
		# Удаление заголовка авторизации в нижнем регистре.
		if "authorization" in headers.keys(): del headers["authorization"]
		# Подстановка токена.
		headers["Authorization"] = self.get_access_token()
		# Отправка GET-запроса.
		Response = self.__Session.post(url, headers = headers, params = params, json = json)
		
		return Response
	
	def refresh_access_token(self):
		"""
		Обновляет токен доступа Авито.
		"""
		
		# Параметры запроса.
		Params = {
			"grant_type": "client_credentials",
			"client_id": self.__ClientID,
			"client_secret": self.__ClientSecret
		}
		# Заголовки запроса.
		Headers = {
			"Content-Type": "application/x-www-form-urlencoded"
		}
		# Запрос нового токена доступа.
		Response = self.__Session.post("https://api.avito.ru/token/", headers = Headers, params = Params)
		
		# Проверка ответа.
		if Response.status_code == 200:
			# Интерпретация ответа в словарь.
			self.__AccessToken = dict(json.loads(Response.text))
			
			# Если запрос содержит ошибку.
			if "error" in self.__AccessToken.keys():
				# Запись в лог ошибки: не удалось обновить токен доступа.
				if self.__Logging: logging.error(f"Profile: {self.__ProfileID}. Unable to refresh access token. Description: \"" + self.__AccessToken["error_description"].rstrip('.') + "\".")
				# Обнуление токена доступа.
				self.__AccessToken = None
				
			else:
				# Запись в лог сообщения: токен обновлён.
				if self.__Logging: logging.info(f"Profile: {self.__ProfileID}. Token refreshed.")
		else:
			# Запись в лог ошибки: не удалось обновить токен доступа.
			if self.__Logging: logging.error(f"Profile: {self.__ProfileID}. Unable to refresh access token. Response code: " + str(Response.status_code) + ".")
			# Обнуление токена доступа.
			self.__AccessToken = None

	def request(self, method: str, url: str, headers: dict | None = None, params: dict | None = None, json: dict | None = None) -> requests.Response:
		"""
		Отправляет запрос с автоматической подстановкой токена доступа.
			method – тип HTTP-запроса;
			url – адрес запроса;
			headers – заголовки запроса;
			params – параметры запроса;
			json – словарь для сериализации в JSON и отправки в качестве тела запроса.
		"""
		
		# Инициализация загловков.
		if headers == None: headers = dict()
		# Удаление заголовка авторизации в нижнем регистре.
		if "authorization" in headers.keys(): del headers["authorization"]
		# Подстановка токена.
		headers["Authorization"] = self.get_access_token()
		# Отправка GET-запроса.
		Response = self.__Session.request(method = method.upper(), url = url, headers = headers, params = params, json = json)
		
		return Response