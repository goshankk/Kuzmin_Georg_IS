from sqlmodel import SQLModel, create_engine, Session, Field

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

def fetch_all_data():
    """
    Получает все данные из таблиц Guest, Booking, Hotel и Room.

    :return: Словарь с данными из всех таблиц.
    """
    with Session(engine) as session:
        guests = session.query(Guest).all()  # Получаем всех гостей
        bookings = session.query(Booking).all()  # Получаем все бронирования
        hotels = session.query(Hotel).all()  # Получаем все гостиницы
        rooms = session.query(Room).all()  # Получаем все номера

    return {
        "guests": guests,
        "bookings": bookings,
        "hotels": hotels,
        "rooms": rooms
    }

# Пример использования функции
if __name__ == "__main__":
    data = fetch_all_data()

    # Выводим информацию о гостях
    print("Гости:")
    for guest in data["guests"]:
        print(guest)

    # Выводим информацию о бронированиях
    print("\nБронирования:")
    for booking in data["bookings"]:
        print(booking)

    # Выводим информацию о гостиницах
    print("\nГостиницы:")
    for hotel in data["hotels"]:
        print(hotel)

    # Выводим информацию о номерах
    print("\nНомера:")
    for room in data["rooms"]:
        print(room)