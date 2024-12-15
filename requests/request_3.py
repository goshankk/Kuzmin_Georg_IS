# Запрос, проверяющий на какие даты забронирована комната по ее номеру

import sqlite3

# Задаем ID комнаты для проверки
room_id_to_check = 101  # Замените на нужный ID комнаты

# Создаем подключение к базе данных
conn = sqlite3.connect('hotel_database.db')
cursor = conn.cursor()

# Запрос для получения дат бронирования по ID номера
query = '''
SELECT Дата_заезда, Дата_выезда, Статус_бронирования
FROM Booking
WHERE id_Номер = ?
'''

# Выполнение запроса
cursor.execute(query, (room_id_to_check,))
bookings = cursor.fetchall()  # Получаем все бронирования для указанного номера

# Закрываем соединение
conn.close()

# Проверяем результат и выводим информацию
if bookings:
    print(f"Даты бронирования для комнаты {room_id_to_check}:")
    for booking in bookings:
        check_in, check_out, status = booking
        print(f"Заезд: {check_in}, Выезд: {check_out}, Статус: {status}")
else:
    print(f"Комната с ID {room_id_to_check} не имеет бронирований.")