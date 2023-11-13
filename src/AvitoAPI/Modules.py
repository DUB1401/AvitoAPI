from AvitoAPI.Types.ShortTermRent import Discounts, Instant

import requests

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