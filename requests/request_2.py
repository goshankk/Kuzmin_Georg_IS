# Запрос проверяющие занята ли комната определенного типа в указанные даты

import sqlite3
from datetime import date

# Функция для проверки занятости комнаты
def is_room_available(room_type: str, check_in: date, check_out: date) -> bool:
    # Создаем подключение к базе данных
    conn = sqlite3.connect('hotel_database.db')
    cursor = conn.cursor()

    # Запрос для проверки занятости
    query = '''
    SELECT COUNT(*)
    FROM Room
    WHERE Тип = ? AND id_Номер NOT IN (
        SELECT id_Номер
        FROM Booking
        WHERE (Дата_заезда < ?) AND (Дата_выезда > ?)
    )
    '''

    # Выполнение запроса
    cursor.execute(query, (room_type, check_out, check_in))
    result = cursor.fetchone()[0]  # Получаем количество свободных комнат

    # Закрываем соединение
    conn.close()

    return result > 0  # Если есть хотя бы одна свободная комната, возвращаем True

# Пример использования функции
if __name__ == '__main__':
    room_type_to_check = "Стандарт"
    check_in_date = date(2024, 12, 20)
    check_out_date = date(2024, 12, 25)

    available = is_room_available(room_type_to_check, check_in_date, check_out_date)
    if available:
        print(f"Комната типа '{room_type_to_check}' доступна с {check_in_date} по {check_out_date}.")
    else:
        print(f"Комната типа '{room_type_to_check}' занята с {check_in_date} по {check_out_date}.")