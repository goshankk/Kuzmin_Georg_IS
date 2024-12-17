from sqlmodel import SQLModel, create_engine, Session, select, Field
from datetime import date

# Определяем модели для таблиц (как в предыдущих примерах)
class Guest(SQLModel, table=True):
    id_Гостя: int = Field(default=None, primary_key=True)
    Имя: str 
    Фамилия: str 
    Номер_телефона: str 
    Email: str 
    Дата_рождения: str 
    Паспорт: str 

class Booking(SQLModel, table=True):
    id_Бронирования: int = Field(default=None, primary_key=True)
    id_Номер: int = Field(default=None, foreign_key="Room.id_Номер")
    id_Гостя: int = Field(default=None, foreign_key="Guest.id_Гостя")
    Дата_заезда: str 
    Дата_выезда: str 
    Статус_бронирования: str 

class Hotel(SQLModel, table=True):
    id_Гостиницы: int = Field(default=None, primary_key=True)
    Название: str 
    Адрес: str 
    Номер_телефона: str 
    Общее_количество_номеров: int
    Дополнительная_информация: str 

class Room(SQLModel, table=True):
    id_Номер: int = Field(default=None, primary_key=True)
    id_Гостиницы: int = Field(default=None, foreign_key="Hotel.id_Гостиницы")
    Тип: str 
    Статус: str 
    Цена_за_ночь: float 
    Дополнительная_информация: str 

# Создаем подключение к базе данных
engine = create_engine('sqlite:///hotel_database.db')

def is_room_available(room_type: str, check_in: date, check_out: date) -> bool:
    """
    Проверяет, доступна ли комната определенного типа в указанные даты.
    """
    with Session(engine) as session:
        # Запрос для проверки занятости
        statement = select(Room).where(
            Room.Тип == room_type,
            Room.id_Номер.not_in(
                select(Booking.id_Номер).where(
                    (Booking.Дата_заезда < check_out) & 
                    (Booking.Дата_выезда > check_in)
                )
            )
        )
        
        available_rooms = session.exec(statement).all()  # Получаем все доступные комнаты

    return len(available_rooms) > 0  # Если есть хотя бы одна свободная комната, возвращаем True

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