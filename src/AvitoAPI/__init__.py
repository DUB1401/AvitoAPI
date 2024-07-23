import logging
from logging import NullHandler

# Инициализация модуля ведения логов.
Logger = logging.getLogger(__name__)
Logger.addHandler(NullHandler())
Logger.setLevel(logging.NOTSET)