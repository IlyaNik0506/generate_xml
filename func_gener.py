from datetime import datetime
import random

def random_number(x):
    # Генерируем 24 случайные цифры от 0 до 9
    random_digits = [str(random.randint(0, 9)) for _ in range(x)]
    random_number_str = ''.join(random_digits)
       
    return random_number_str


def date_time():
    # Получаем текущую дату и время
    current_datetime = datetime.now()
    # Форматируем дату и время в нужный формат
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S') 
    return formatted_datetime