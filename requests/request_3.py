import sqlite3

def check_room_bookings(room_id: int):
    """
    Проверяет, на какие даты забронирована комната по ее номеру.

    :param room_id: ID комнаты для проверки.
    :param db_name: Имя файла базы данных (по умолчанию 'hotel_database.db').
    :return: Список кортежей с датами заезда и выезда, а также статусом бронирования.
    """
    # Создаем подключение к базе данных
    conn = sqlite3.connect('..\hotel_database.db')
    cursor = conn.cursor()

    # Запрос для получения дат бронирования по ID номера
    query = '''
    SELECT Дата_заезда, Дата_выезда, Статус_бронирования
    FROM Booking
    WHERE id_Номер = ?
    '''

    # Выполнение запроса
    cursor.execute(query, (room_id,))
    bookings = cursor.fetchall()  # Получаем все бронирования для указанного номера

    # Закрываем соединение
    conn.close()

    return bookings

# Пример использования функции
if __name__ == "__main__":
    room_id_to_check = 101  # Замените на нужный ID комнаты
    bookings = check_room_bookings(room_id_to_check)

    # Проверяем результат и выводим информацию
    if bookings:
        print(f"Даты бронирования для комнаты {room_id_to_check}:")
        for booking in bookings:
            check_in, check_out, status = booking
            print(f"Заезд: {check_in}, Выезд: {check_out}, Статус: {status}")
    else:
        print(f"Комната с ID {room_id_to_check} не имеет бронирований.")