class Balance:
	"""
	Баланс профиля.
	"""
	
	#==========================================================================================#
	# >>>>> СВОЙСТВА ТОЛЬКО ДЛЯ ЧТЕНИЯ <<<<< #
	#==========================================================================================#

	@property
	def bonus(self) -> int:
		"""
		Бонус.
		"""
		
		return self.__Bonus
	
	@property
	def real(self) -> int:
		"""
		Реальные средства.
		"""

		return self.__Real
	
	#==========================================================================================#
	# >>>>> ПУБЛИЧНЫЕ МЕТОДЫ <<<<< #
	#==========================================================================================#

	def __init__(self, real: int, bonus: int):
		"""
		Баланс профиля.
		"""

		#---> Генерация динамических свойств.
		#==========================================================================================#
		# Бонус.
		self.__Bonus = bonus
		# Реальные средства.
		self.__Real = real