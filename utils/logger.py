import logging
import sys
from logging.handlers import RotatingFileHandler


# Настройка логирования
logger = logging.getLogger('telegram_posting_bot')
logger.setLevel(logging.INFO) #Поменять в проде на ERROR

# Создаем обработчик для вывода в файл
file_handler = RotatingFileHandler(
    'bot.log',
    maxBytes=5242880,  # 5MB
    backupCount=3,
    encoding='utf-8'
)
file_handler.setLevel(logging.INFO)

# Создаем обработчик для вывода в консоль
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

# Создаем форматтер
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Добавляем обработчики к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)