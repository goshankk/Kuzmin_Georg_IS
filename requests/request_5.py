import sqlite3

def get_bookings_within_dates(check_in: str, check_out: str):
    """
    Получает информацию о бронированиях, которые пересекаются с заданными датами.

    :param check_in: Дата заезда в формате 'YYYY-MM-DD'.
    :param check_out: Дата выезда в формате 'YYYY-MM-DD'.
    :return: Список кортежей с информацией о бронированиях.
    """
    # Создаем подключение к базе данных
    conn = sqlite3.connect('..\hotel_database.db')
    cursor = conn.cursor()

    # SQL-запрос для получения информации о бронированиях
    query = '''
    SELECT Booking.id_Бронирования, Guest.Имя, Guest.Фамилия, Booking.Дата_заезда, Booking.Дата_выезда, Booking.id_Номер
    FROM Booking
    JOIN Guest ON Booking.id_Гостя = Guest.id_Гостя
    WHERE Booking.Дата_заезда < ? AND Booking.Дата_выезда > ?;
    '''

    # Выполнение запроса с параметрами
    cursor.execute(query, (check_out, check_in))
    results = cursor.fetchall()  # Получаем все результаты

    # Закрываем соединение
    conn.close()

    return results

# Пример использования функции
if __name__ == "__main__":
    check_in_date = '2024-12-20'  # Замените на нужную дату заезда
    check_out_date = '2024-12-25'  # Замените на нужную дату выезда

    bookings = get_bookings_within_dates(check_in_date, check_out_date)


    print(f"Информаци о бронировании номеров в следующие даты {check_in_date} - {check_out_date}")
    # Выводим результаты
    for row in bookings:
        print(f"\nФИО: {row[1]} {row[2]}\nНомер: {row[5]} \nДата заезда: {row[3]} \nДата выезда: {row[4]}")