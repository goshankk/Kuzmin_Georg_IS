# Получение списка всех гостей с их бронированиями
import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('hotel_database.db')

# Создаем курсор для выполнения SQL-запросов
cursor = conn.cursor()

# Запрос для получения списка всех гостей с их бронированиями
query = '''
SELECT Guest.Имя, Guest.Фамилия, Booking.Дата_заезда, Booking.Дата_выезда, Booking.Статус_бронирования
FROM Guest
LEFT JOIN Booking ON Guest.id_Гостя = Booking.id_Гостя
'''

# Выполнение запроса
cursor.execute(query)

# Получение результатов
results = cursor.fetchall()

# Вывод результатов
print("Список гостей с их бронированиями:")
for row in results:
    имя, фамилия, дата_заезда, дата_выезда, статус = row
    print(f"Гость: {имя} {фамилия}, Заезд: {дата_заезда}, Выезд: {дата_выезда}, Статус: {статус}")

# Закрываем соединение
conn.close()