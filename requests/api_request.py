#from typing import Union

from request_1 import fetch_all_data                 # Выводит все данные из базы данных
from request_2 import is_room_available, date        # Запрос проверяющие занята ли комната определенного типа в указанные даты
from request_3 import create_booking                 # Добавляет запись бронирования
from request_4 import delete_booking                 # Получает список всех гостей с их бронированиями
from request_5 import update_booking_status 

from fastapi import FastAPI, HTTPException

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
@app.get("/create_booking/{room_id}/{id_гостя}/{дата_заезд}/{дата_выезда}/{статус}")
def create_books(room_id, id_гостя, дата_заезд, дата_выезда, статус):
    bookings = create_booking(room_id, id_гостя, дата_заезд, дата_выезда, статус)
    # Проверяем результат и выводим информацию
    if bookings:
        return bookings 
    else:
        return (f"Комната с номером {room_id} не имеет бронирований.")


@app.delete("/bookings/{booking_id}")
def remove_booking(booking_id: int):
    success = delete_booking(booking_id)
    if success:
        return {"message": f"Бронирование с ID {booking_id} успешно удалено."}
    else:
        raise HTTPException(status_code=404, detail="Бронирование не найдено.")


@app.put("/bookings/{booking_id}/status")
def change_booking_status(booking_id: int, new_status: str):
    success = update_booking_status(booking_id, new_status)
    if success:
        return {"message": f"Статус бронирования с ID {booking_id} успешно обновлен на '{new_status}'."}
    else:
        raise HTTPException(status_code=404, detail="Бронирование не найдено.")