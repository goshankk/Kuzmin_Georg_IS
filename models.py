import sqlite3

# Создаем подключение к базе данных (если базы данных нет, она будет создана)
conn = sqlite3.connect('hotel_database.db')

# Создаем курсор для выполнения SQL-запросов
cursor = conn.cursor()

# Создаем таблицу Гости
cursor.execute('''
CREATE TABLE IF NOT EXISTS Guest (
    id_Гостя INTEGER NOT NULL PRIMARY KEY,
    Имя TEXT DEFAULT '50',
    Фамилия TEXT DEFAULT '50',
    Номер_телефона TEXT DEFAULT '15',
    Email TEXT DEFAULT '100',
    Дата_рождения DATE,
    Паспорт TEXT DEFAULT '20'
)
''')

# Заполнение таблицы Гости
guests = [
    (1, 'Иван', 'Иванов', '1234567890', 'ivan@example.com', '1990-01-01', 'AB123456'),
    (2, 'Петр', 'Петров', '0987654321', 'petr@example.com', '1985-05-05', 'CD789012'),
    (3, 'Светлана', 'Сидорова', '1122334455', 'svetlana@example.com', '1992-03-03', 'EF345678')
]

cursor.executemany('''
INSERT INTO Guest (id_Гостя, Имя, Фамилия, Номер_телефона, Email, Дата_рождения, Паспорт)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', guests)

# Создаем таблицу Бронирования
cursor.execute('''
CREATE TABLE IF NOT EXISTS Booking (
    id_Бронирования INTEGER NOT NULL PRIMARY KEY,
    id_Номер INTEGER,
    id_Гостя INTEGER,
    Дата_заезда DATE,
    Дата_выезда DATE,
    Статус_бронирования TEXT DEFAULT '20',
    FOREIGN KEY (id_Номер) REFERENCES Номера(id_Номер),
    FOREIGN KEY (id_Гостя) REFERENCES Гости(id_Гостя)
)
''')

# Заполнение таблицы Бронирования
bookings = [
    (1, 101, 1, '2024-12-20', '2024-12-25', 'Подтверждено'),
    (2, 102, 2, '2024-12-22', '2024-12-27', 'Ожидает подтверждения'),
    (3, 103, 3, '2024-12-24', '2024-12-29', 'Отменено'),
    (4, 101, 2, '2024-12-27', '2024-12-31', 'Подтверждено'),
]

cursor.executemany('''
INSERT INTO Booking (id_Бронирования, id_Номер, id_Гостя, Дата_заезда, Дата_выезда, Статус_бронирования)
VALUES (?, ?, ?, ?, ?, ?)
''', bookings)

"""
# Создаем таблицу Персонал
cursor.execute('''
CREATE TABLE IF NOT EXISTS Персонал (
    id_Гостиницы INTEGER,
    id_сотрудника INTEGER NOT NULL PRIMARY KEY,
    Имя TEXT DEFAULT '50',
    Фамилия TEXT DEFAULT '50',
    Должность TEXT DEFAULT '50',
    FOREIGN KEY (id_Гостиницы) REFERENCES Гостиницы(id_Гостиницы)
)
''')

# Заполнение таблицы Персонал
staff = [
    (1, 1, 'Алексей', 'Алексеев', 'Менеджер'),
    (2, 1, 'Мария', 'Маркова', 'Ресепшен'),
    (3, 1, 'Дмитрий', 'Дмитриев', 'Уборщик')
]

cursor.executemany('''
INSERT INTO Персонал (id_Гостиницы, id_сотрудника, Имя, Фамилия, Должность)
VALUES (?, ?, ?, ?, ?)
''', staff)
"""
# Создаем таблицу Гостиницы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Hotel (
    id_Гостиницы INTEGER NOT NULL PRIMARY KEY,
    Название TEXT DEFAULT '50',
    Адрес TEXT DEFAULT '20',
    Номер_телефона TEXT DEFAULT '15',
    Общее_количество_номеров INTEGER NOT NULL,
    Дополнительная_информация TEXT
)
''')

# Заполнение таблицы Гостиницы
hotels = [
    (1, 'Гостиница Солнце', 'Улица Солнечная, 1', '123456789', 50, 'Бесплатный Wi-Fi'),
    (2, 'Гостиница Луна', 'Улица Лунная, 2', '987654321', 30, 'Завтрак включен')
]

cursor.executemany('''
INSERT INTO Hotel (id_Гостиницы, Название, Адрес, Номер_телефона, Общее_количество_номеров, Дополнительная_информация)
VALUES (?, ?, ?, ?, ?, ?)
''', hotels)


# Создаем таблицу Номера
cursor.execute('''
CREATE TABLE IF NOT EXISTS Room (
    id_Номер INTEGER NOT NULL PRIMARY KEY,
    id_гос INTEGER,
    id_Гостиницы INTEGER,
    Тип TEXT DEFAULT '50',
    Статус TEXT DEFAULT '20',
    Цена_за_ночь DECIMAL(18, 0),
    Дополнительная_информация TEXT,
    FOREIGN KEY (id_гос) REFERENCES Номера(id_Номер),
    FOREIGN KEY (id_Гостиницы) REFERENCES Гостиницы(id_Гостиницы)
)
''')

# Заполнение таблицы Номера
rooms = [
    (101, None, 1, 'Стандарт', 'Свободен', 3000, 'С видом на море'),
    (102, None, 1, 'Люкс', 'Занят', 6000, 'С балконом'),
    (103, None, 2, 'Эконом', 'Свободен', 2000, 'Без окна')
]

cursor.executemany('''
INSERT INTO Room (id_Номер, id_гос, id_Гостиницы, Тип, Статус, Цена_за_ночь, Дополнительная_информация)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', rooms)

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()