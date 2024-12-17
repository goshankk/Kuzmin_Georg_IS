from sqlmodel import SQLModel, Field

# Определяем модели для таблиц (как в предыдущем примере)
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
    id_гос: int = Field(default=None, foreign_key="Guest.id_Гостя")
    id_Гостиницы: int = Field(default=None, foreign_key="Hotel.id_Гостиницы")
    Тип: str 
    Статус: str 
    Цена_за_ночь: float 
    Дополнительная_информация: str 

# Создаем подключение к базе данных 
# engine = create_engine('sqlite:///hotel_database.db')

