#from typing import Union

from request_1 import fetch_all_data                 # Выводит все данные из базы данных
from request_2 import is_room_available, date              # Запрос проверяющие занята ли комната определенного типа в указанные даты
from request_3 import check_room_bookings            # Проверяет, на какие даты забронирована комната по ее номеру
from request_4 import fetch_guests_with_bookings     # Получает список всех гостей с их бронированиями
from request_5 import get_bookings_within_dates      # Получает информацию о бронированиях, которые пересекаются с заданными датами


from fastapi import FastAPI

app = FastAPI()

# Проверка запроса:
# http://127.0.0.1:8000/alldata
@app.get("/alldata")
def read_root():
    data = fetch_all_data()
    return {"guests": data["guests"],
            "bookings": data["bookings"],
            "hotels": data["hotels"],
            "rooms": data["rooms"]}

# Проверка запроса:
# http://127.0.0.1:8000/room_available/Стандарт/2024-12-20/2024-12-25
@app.get("/room_available/{room_type}/{check_in}/{check_out}")
def read_item(room_type: str, check_in: date, check_out: date):
    available = is_room_available(room_type, check_in, check_out)
    if available:
        return (f"Комната типа '{room_type}' доступна с {check_in} по {check_out}.")
    else:
        return (f"Комната типа '{room_type}' занята с {check_in} по {check_out}.")

# Проверка запроса:
# http://127.0.0.1:8000/check_room/101
# http://127.0.0.1:8000/check_room/500
@app.get("/check_room/{room_id}")
def update_item(room_id: int):
    bookings = check_room_bookings(room_id)
    # Проверяем результат и выводим информацию
    if bookings:
        return bookings 
    else:
        return (f"Комната с номером {room_id} не имеет бронирований.")

# Проверка запроса:
# http://127.0.0.1:8000/fetch_guests
@app.get("/fetch_guests")
def update_item():
    guests = fetch_guests_with_bookings()
    return guests

# Проверка запроса:
# http://127.0.0.1:8000/get_bookings/2024-12-20/2024-12-25
# http://127.0.0.1:8000/get_bookings/2024-12-20/2024-12-28
@app.get("/get_bookings/{check_in}/{check_out}")
def update_item(check_in: str, check_out: str):
    bookings = get_bookings_within_dates(check_in, check_out)
    return bookings