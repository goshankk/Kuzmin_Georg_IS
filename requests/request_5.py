
from sqlmodel import SQLModel, Field, create_engine, Session, select

# Определяем модели для таблиц (как в вашем коде)
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

# Создаем подключение к базе данных
engine = create_engine('sqlite:///hotel_database.db')

app = FastAPI()

def update_booking_status(booking_id: int, new_status: str) -> bool:
    """
    Обновляет статус бронирования по ID.

    :param booking_id: ID записи бронирования для обновления.
    :param new_status: Новый статус бронирования.
    :return: True, если статус был успешно обновлен, иначе False.
    """
    with Session(engine) as session:
        statement = select(Booking).where(Booking.id_Бронирования == booking_id)
        booking = session.exec(statement).first()

        if booking:
            booking.Статус_бронирования = new_status
            session.add(booking)  # Обновляем запись
            session.commit()  # Сохраняем изменения
            return True
        else:
            return False  # Запись не найдена
