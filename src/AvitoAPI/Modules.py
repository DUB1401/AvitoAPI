from AvitoAPI.Types.ShortTermRent import *

import datetime
import requests
import json

class ShortTermRent:
	"""
	Модуль API: краткосрочная аренда.
	"""
	
	def __init__(self, profile: int | str, request_method: any):
		"""
		Модуль API: краткосрочная аренда.
			profile – номер профиля Авито;
			request_method – указатель на метод выполнения запросов.
		"""

		#---> Генерация динамических свойств.
		#==========================================================================================#
		# Номер профиля авито.
		self.__Profile = int(profile)
		# Метод выполнения запросов.
		self.__Request = request_method
		
	def get_bookings(
			self,
			item_id: int | str,
			date_start: datetime.datetime,
			date_end: datetime.datetime,
			with_unpaid: bool = True
		) -> list[Booking] | None:
		
		"""
		Возвращает список броней по объявлению.
			item_id – идентификатор объявления;
			date_start – дата начала выборки;
			date_end – дата окончания выборки;
			with_unpaid – указывает, добавлять ли в выборку неоплаченные брони.
		"""
		# Параметры запроса.
		Params = {
			"date_start": str(date_start.date()),
			"date_end": str(date_end.date()),
			"with_unpaid": with_unpaid
		}
		# Выполнение запроса.
		Response = self.__Request("GET", f"https://api.avito.ru/realty/v1/accounts/{self.__Profile}/items/{item_id}/bookings", params = Params)
		
		# Если запрос успешен.
		if Response.status_code == 200: 
			# Буфер преобразования.
			Bufer = list()
			# Полученные данные.
			Data = json.loads(Response.text)
			
			# Для каждого элемента.
			for Element in Data["bookings"]:
				# Сохранить преобразованные в объект данные.
				Bufer.append(Booking(Element))
				
			# Перезапись ответа буфером.
			Response = Bufer
		
		else:
			# Обнуление запроса.
			Response = None
		
		return Response
		
	def fill_estate_calendar(
			self,
			item_id: int | str,
		    bookings: BookingsDates
		) -> requests.Response:
		"""
		Заполняет календарь занятости объекта недвижимости.
			item_id – идентификатор объявления;
			bookings – даты бронирования объекта недвижимости.
		"""

		# Выполнение запроса.
		Response = self.__Request("POST", f"https://api.avito.ru/core/v1/accounts/{self.__Profile}/items/{item_id}/bookings", json = {"bookings": bookings.get()})
		
		return Response
		
	def set_base_params(
			self,
		    item_id: int | str,
		    discounts: Discounts | None = None,
		    extra_guest_fee: int | None = None,
		    instant: Instant | None = None,
		    minimal_duration: int = None,
		    night_price: int | None = None,
		    refund: int | None = None
			
		) -> requests.Response:
		"""
		Задаёт базовые параметры.
			item_id – идентификатор объявления;
			discounts – список скидок для забронировавших определённое количество ночей;
			extra_guest_fee – стоимость доплаты за каждого гостя сверх одного;
			instant – параметры мгновенного бронирования;
			minimal_duration – минимальное количество ночей для бронирования;
			refund – количество дней, за которое можно отказаться от брони.
			
		"""
		
		# Тело запроса.
		Body = dict()
		# Заполнение тела.
		if type(discounts) == Discounts: Body["discount"] = discounts.get()
		if extra_guest_fee != None: Body["extra_guest_fee"] = int(extra_guest_fee)
		if type(instant) == Instant: Body["instant"] = instant.get()
		if minimal_duration != None: Body["minimal_duration"] = int(minimal_duration)
		if night_price != None: Body["night_price"] = int(night_price)
		if refund != None: Body["refund"] = {"days": int(refund)}
		# Выполнение запроса.
		Response = self.__Request("POST", f"https://api.avito.ru/realty/v1/items/{item_id}/base", json = Body)
		
		return Response