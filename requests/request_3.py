from sqlmodel import SQLModel, Field, create_engine, Session

# Определяем модели для таблиц
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

def create_booking(id_номер: int, id_гостя: int, дата_заезда: str, дата_выезда: str, статус: str) -> Booking:
    """
    Создает новую запись в таблице Booking.
    """
    new_booking = Booking(
        id_Номер=id_номер,
        id_Гостя=id_гостя,
        Дата_заезда=дата_заезда,
        Дата_выезда=дата_выезда,
        Статус_бронирования=статус
    )

    with Session(engine) as session:
        session.add(new_booking)  # Добавляем новую запись
        session.commit()  # Сохраняем изменения
        session.refresh(new_booking)  # Обновляем объект, чтобы получить его ID

    return new_booking

# Пример использования функции
if __name__ == '__main__':
    booking = create_booking(
        id_номер=101,  # Замените на реальный ID номера
        id_гостя=2,  # Замените на реальный ID гостя
        дата_заезда='2024-12-30',
        дата_выезда='2024-12-31',
        статус='Подтверждено'
    )
    print(f"Бронирование создано: {booking}")