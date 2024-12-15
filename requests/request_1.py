# Запрос выводящий все данные из базы данных
import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('hotel_database.db')
cursor = conn.cursor()

# Запрос для выборки всех гостей
cursor.execute('SELECT * FROM Guest')
guests = cursor.fetchall()  # Получаем всех гостей

# Запрос для выборки всех бронирований
cursor.execute('SELECT * FROM Booking')
bookings = cursor.fetchall()  # Получаем все бронирования

# Запрос для выборки всех гостиниц
cursor.execute('SELECT * FROM Hotel')
hotels = cursor.fetchall()  # Получаем все гостиницы

# Запрос для выборки всех номеров
cursor.execute('SELECT * FROM Room')
rooms = cursor.fetchall()  # Получаем все номера

# Закрываем соединение
conn.close()

# Выводим информацию о гостях
print("Гости:")
for guest in guests:
    print(guest)

# Выводим информацию о бронированиях
print("\nБронирования:")
for booking in bookings:
    print(booking)

# Выводим информацию о гостиницах
print("\nГостиницы:")
for hotel in hotels:
    print(hotel)

# Выводим информацию о номерах
print("\nНомера:")
for room in rooms:
    print(room)