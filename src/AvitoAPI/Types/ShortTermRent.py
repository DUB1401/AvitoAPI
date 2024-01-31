import datetime

#==========================================================================================#
# >>>>> ВЛОЖЕННЫЕ ТИПЫ ДАННЫХ <<<<< #
#==========================================================================================#

class Contact:
	"""
	Контакты забронировавшего пользователя.
	"""
		
	#==========================================================================================#
	# >>>>> СВОЙСТВА ТОЛЬКО ДЛЯ ЧТЕНИЯ <<<<< #
	#==========================================================================================#

	@property
	def email(self) -> str | None:
		"""
		Электронная почта забронировавшего пользователя.
		"""
		
		# Электронная почта забронировавшего пользователя.
		Property = self.__ContactData["email"] if "email" in self.__ContactData.keys() else None
		
		return Property
		
	@property
	def name(self) -> str | None:
		"""
		Имя забронировавшего пользователя.
		"""
		
		# Имя забронировавшего пользователя.
		Property = self.__ContactData["name"] if "name" in self.__ContactData.keys() else None
		
		return Property
		
	@property
	def phone(self) -> str | None:
		"""
		Номер телефона забронировавшего пользователя.
		"""
		
		# Номер телефона забронировавшего пользователя.
		Property = self.__ContactData["phone"] if "phone" in self.__ContactData.keys() else None
		
		return Property
			
	#==========================================================================================#
	# >>>>> МЕТОДЫ <<<<< #
	#==========================================================================================#

	def __init__(self, Data: dict):
		"""
		Контакты забронировавшего пользователя.
		"""

		#---> Генерация динамических свойств.
		#==========================================================================================#
		# Словарь контактов забронировавшего пользователя.
		self.__ContactData = Data
		
class SafeDeposit:
	"""
	Задаток.
	"""
	
	#==========================================================================================#
	# >>>>> СВОЙСТВА ТОЛЬКО ДЛЯ ЧТЕНИЯ <<<<< #
	#==========================================================================================#

	@property
	def owner_amount(self) -> str | None:
		# Электронная почта забронировавшего пользователя.
		Property = self.__SafeDepositData["owner_amount"] if "owner_amount" in self.__SafeDepositData.keys() else None
		
		return Property
		
	@property
	def tax(self) -> str | None:
		# Имя забронировавшего пользователя.
		Property = self.__SafeDepositData["tax"] if "tax" in self.__SafeDepositData.keys() else None
		
		return Property
		
	@property
	def total_amount(self) -> str | None:
		# Номер телефона забронировавшего пользователя.
		Property = self.__SafeDepositData["total_amount"] if "total_amount" in self.__SafeDepositData.keys() else None
		
		return Property
			
	#==========================================================================================#
	# >>>>> МЕТОДЫ <<<<< #
	#==========================================================================================#

	def __init__(self, Data: dict):
		"""
		Задаток.
		"""
	
		#---> Генерация динамических свойств.
		#==========================================================================================#
		# Словарь данных.
		self.__SafeDepositData = Data

#==========================================================================================#
# >>>>> ТИПЫ ДАННЫХ <<<<< #
#==========================================================================================#

class Booking:
	"""
	Описание свойств брони объекта недвижимости.
	"""
	
	#==========================================================================================#
	# >>>>> СВОЙСТВА ТОЛЬКО ДЛЯ ЧТЕНИЯ <<<<< #
	#==========================================================================================#

	@property
	def avito_booking_id(self) -> int | None:
		"""
		Идентификатор брони.
		"""
		
		# Базовая стоимость.
		Property = self.__BookingData["avito_booking_id"] if "avito_booking_id" in self.__BookingData.keys() else None
		
		return Property
	
	@property
	def base_price(self) -> int | None:
		"""
		Базовая стоимость.
		"""
		
		# Базовая стоимость.
		Property = self.__BookingData["base_price"] if "base_price" in self.__BookingData.keys() else None

		return Property
	
	@property
	def check_in(self) -> datetime.datetime:
		"""
		Дата заселения.
		"""
		
		# Преобразование даты.
		Year, Month, Day = self.__BookingData["check_in"].split("-")
		# Дата заселения.
		Property = datetime.datetime(int(Year), int(Month), int(Day))
		
		return Property
	
	@property
	def check_out(self) -> datetime.datetime:
		"""
		Дата выселения.
		"""
		
		# Преобразование даты.
		Year, Month, Day = self.__BookingData["check_out"].split("-")
		# Дата выселения.
		Property = datetime.datetime(int(Year), int(Month), int(Day))
		
		return Property
	
	@property
	def contact(self) -> Contact | None:
		"""
		Контакты забронировавшего пользователя.
		"""
		
		# Контакты забронировавшего пользователя.
		Property = None
		# Преобразование контакта в класс.
		if "contact" in self.__BookingData.keys(): Property = Contact(self.__BookingData["contact"])
		
		return Property
	
	@property
	def guest_count(self) -> int | None:
		"""
		Количество гостей.
		"""
		
		# Количество гостей.
		Property = self.__BookingData["guest_count"] if "guest_count" in self.__BookingData.keys() else None

		return Property
	
	@property
	def nights(self) -> int | None:
		"""
		Количество забронированных ночей.
		"""
		
		# Количество забронированных ночей.
		Property = self.__BookingData["nights"] if "nights" in self.__BookingData.keys() else None

		return Property
	
	@property
	def safe_deposit(self) -> SafeDeposit | None:
		# Данные предоплаты.
		Property = None
		# Преобразование предоплаты в класс.
		if "safe_deposit" in self.__BookingData.keys(): Property = SafeDeposit(self.__BookingData["safe_deposit"])
		
		return Property
	
	@property
	def status(self) -> bool | None:
		"""
		Статус брони.
		"""
		
		# Статус брони.
		Property = True if "status" in self.__BookingData["status"] == "active" else False

		return Property
	
	#==========================================================================================#
	# >>>>> ПУБЛИЧНЫЕ МЕТОДЫ <<<<< #
	#==========================================================================================#

	def __init__(self, Data: dict):
		"""
		Описание свойств брони объекта недвижимости.
		"""

		#---> Генерация динамических свойств.
		#==========================================================================================#
		# Словарь описания брони.
		self.__BookingData = Data

class BookingsDates:
	"""
	Описание дат бронирования объекта недвижимости.
	"""

	def __init__(self):
		"""
		Описание дат бронирования объекта недвижимости.
		"""

		#---> Генерация динамических свойств.
		#==========================================================================================#
		# Список дат броней.
		self.__BookingsDates = list()
		
	def add(self, date_start: datetime.datetime, date_end: datetime.datetime):
		"""
		Задаёт указанный диапазон дат для бронирования.
			date_start – дата начала брони;
			date_end – дата окончания брони.
		"""

		self.__BookingsDates.append({"date_start": str(date_start.date()), "date_end": str(date_end.date())})
		
	def get(self) -> dict:
		"""
		Возвращает описание дат бронирования объекта недвижимости.
		"""

		return self.__BookingsDates
	
class Discounts:
	"""
	Cписок скидок для забронировавших определённое количество ночей.
	"""

	def __init__(self):
		"""
		Cписок скидок для забронировавших определённое количество ночей.
		"""

		#---> Генерация динамических свойств.
		#==========================================================================================#
		# Список ссылок.
		self.__Discounts = list()
		
	def on_3_days(self, percent: int):
		"""
		Дополняет список скидок для забронировавших определённое количество ночей.
			percent – процент скидки.
		"""
		
		self.__Discounts.append({"percent": percent, "threshold": 3})
		
	def on_7_days(self, percent: int):
		"""
		Дополняет список скидок для забронировавших определённое количество ночей.
			percent – процент скидки.
		"""
		
		self.__Discounts.append({"percent": percent, "threshold": 7})
		
	def on_30_days(self, percent: int):
		"""
		Дополняет список скидок для забронировавших определённое количество ночей.
			percent – процент скидки.
		"""
		
		self.__Discounts.append({"percent": percent, "threshold": 30})

	def get(self) -> list[dict]:
		"""
		Возвращает список скидок для забронировавших определённое количество ночей.
		"""

		return self.__Discounts
	
class Instant:
	"""
	Параметры мгновенного бронирования.
	"""

	def __init__(self, max_days: int, min_days: int):
		"""
		Параметры мгновенного бронирования.
			max_days – максимальное количество дней для бронирования;
			min_days – минимальное количество дней для бронирования.
		"""

		#---> Генерация динамических свойств.
		#==========================================================================================#
		# Список ссылок.
		self.__Instant = {
			"active": True,
			"max_days": max_days,
			"min_days": min_days
		}

	def get(self) -> dict:
		"""
		Возвращает параметры мгновенного бронирования.
		"""

		return self.__Instant
	
class RentPeriods:
	"""
	Параметры аренды в диапазонах дат.
	"""

	def __init__(self):
		"""
		Параметры аренды в диапазонах дат.
		"""

		#---> Генерация динамических свойств.
		#==========================================================================================#
		# Список периодов аренды.
		self.__RentPeriods = list()
		
	def add(self, date_from: datetime.datetime, date_to: datetime.datetime, night_price: int, extra_guest_fee: int = 0, minimal_duration: int = 1):
		"""
		Задаёт указанный диапазон дат для бронирования.
			date_from – дата начала настраиваемого периода;
			date_to – дата окончания настраиваемого периода;
			night_price – стоимость;
			extra_guest_fee – доплата за гостя;
			minimal_duration – минимальная длительность аренды.
		"""

		self.__BookingsDates.append({
			"date_from": str(date_from.date()),
			"date_to": str(date_to.date()),
			"extra_guest_fee": extra_guest_fee,
			"minimal_duration": minimal_duration,
			"night_price": night_price
		})
		
	def get(self) -> list[dict]:
		"""
		Возвращает параметры периодов аренды.
		"""

		return self.__RentPeriods