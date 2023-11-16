# AvitoAPI
**AvitoAPI** – это библиотека Python, имплементирующая методы клиентского API сайта [Авито](https://www.avito.ru/) и предоставляющая инструменты для удобной работы с профилями.

Вся документация представлена на Авито в формате Swagger 3.0. Ознакомиться с WEB-версией можно [здесь](https://developers.avito.ru/api-catalog/user/documentation).

> [!WARNING]  
> Библиотека находится в стадии разработки. О прогрессе вы можете узнать ниже.

## Прогресс разработки
- [ ] CPA-аукцион
- [x] Авторизация
	- [x] Получение access token
	- [ ] Получение access token (**не планируется**)
	- [x] Обновление access token
- [ ] Автозагрузка
- [ ] Автостратегия
- [ ] Автотека
- [ ] CallTracking\[КТ\]
- [ ] CPA Авито
- [ ] Доставка (песочница)
- [ ] Объявления
- [ ] Авито.Работа
- [ ] Мессенджер
- [ ] Управление заказами
- [ ] Рейтинги и отзывы
- [ ] Рассылка скидок и спецпредложений в мессенджере (beta-version)
- [ ] Управление остатками
- [x] Краткосрочная аренда
	- [x] Установка базовых параметров
	- [x] Заполнение календаря занятости объекта недвижимости 
	- [x] Получение списка броней по объявлению
	- [ ] Актуализация параметров для выбранных периодов
- [ ] Тарифы
- [ ] Информация о пользователе

## Порядок установки и использования
1. Установить библиотеку при помощи `pip` или скачать папку [AvitoAPI](https://github.com/DUB1401/AvitoAPI/tree/main/src) и поместить её в корневом каталоге скрипта, вручную установив зависимости из файла _pyproject.toml_.
```
pip install git+https://github.com/DUB1401/AvitoAPI
```
2. Перейти в [данный](https://www.avito.ru/professionals/api) раздел сайта и получить бесплатный ID клиента и секретный ключ.
3. Узнать [здесь](https://www.avito.ru/profile/basic) номер профиля Авито.
4. Использовать полученные данные для авторизации и отправки запросов, как показано ниже.

### Пример
```Python
from AvitoAPI.Types.ShortTermRent import Discounts
from AvitoAPI.Profile import Profile

# Номер профиля.
PROFILE_ID = int()
# ID склиента API.
CLIENT_ID = str()
# Секретный ключ клиента API.
CLIENT_SECRET = str()
# ID объявления.
ITEM_ID = int()

# Инициализация профиля для доступа к API.
User = Profile(PROFILE_ID, CLIENT_ID, CLIENT_SECRET)
# Инициализация списка скидок.
ItemDiscounts = Discounts()
# Добавление скидки: 5% при бронировании от 3-ёх ночей.
ItemDiscounts.on_3_days(5)
# Установка базовых параметров для краткосрочно арендуемой квартиры.
Response = User.short_term_rent().set_base_params(ITEM_ID, discounts = ItemDiscounts, night_price = 3500)

# Если запрос успешно выполнен.
if Response.status_code == 200:
	# Вывод в консоль сообщения об успешном выполнении.
	print("Запрос успешно выполнен.")
	
else:
	# Вывод в консоль сообщения об ошибке.
	print(f"Не удалось выполнить запрос. HTTP код: {Response.status_code}.")
```

_Copyright © DUB1401. 2023._
