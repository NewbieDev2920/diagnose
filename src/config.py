import os
from pathlib import Path

BASE_DIR = Path(__file__).parent
print(BASE_DIR)

DB_NAME = 'database.db'
DB_USER = 'abstract_ninja'
DB_HOST = 'localhost'
DB_PASSWORD = 'mypassword'
SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIR/"database"/"database.db"}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLITE_MANUAL_MEDIC_TABLE_CREATION = '''CREATE TABLE IF NOT EXISTS medics (
        medic_id VARCHAR(30) PRIMARY KEY,
        fullname VARCHAR(100),
        email VARCHAR(50),
        cellphone VARCHAR(30),
        user VARCHAR(30),
        password VARCHAR(100),
        register_date VARCHAR(100)
    )'''
