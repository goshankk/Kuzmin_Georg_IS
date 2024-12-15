import sqlite3

def fetch_guests_with_bookings():
    """
    Получает список всех гостей с их бронированиями.

    :param db_name: Имя файла базы данных (по умолчанию 'hotel_database.db').
    :return: Список кортежей с информацией о гостях и их бронированиях.
    """
    # Создаем подключение к базе данных
    conn = sqlite3.connect('..\hotel_database.db')
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

    # Закрываем соединение
    conn.close()

    return results

# Пример использования функции
if __name__ == "__main__":
    guests_with_bookings = fetch_guests_with_bookings()

    # Вывод результатов
    print("Список гостей с их бронированиями:")
    for row in guests_with_bookings:
        имя, фамилия, дата_заезда, дата_выезда, статус = row
        print(f"Гость: {имя} {фамилия}, Заезд: {дата_заезда}, Выезд: {дата_выезда}, Статус: {статус}")