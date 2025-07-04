from flask import Flask
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from src.models.Medic import Medic
from src.models.Patient import Patient
from src.models.Record import Record

class MedicCrudOp:
    def __init__(self, app: Flask, db: SQLAlchemy):
        self._app = app
        self._db = db

    def create_medic(self, medic: Medic) -> None:
        '''
        Insert a medic in the medics table (database.db)
        ```sql
        INSERT INTO table_name (column1, column2, column3, ...)
        VALUES (value1, value2, value3, ...); 
        ```
        '''
        with self._app.app_context():
            self._db.session.add(medic)
            self._db.session.commit()
            print('Medic added.')

    def get_medic(self, id: str) -> Medic:
        with self._app.app_context():
            medic = self._db.session.get(Medic, id)
            self._db.session.commit()
            return medic

    def get_medic_id(self, fullname: str):
        pass

    def update_medic(self, id: str):
        pass

    def delete_medic(self, id: str):
        pass

    def debug_get_all_medic(self):
        return self._db.session.execute(text('SELECT * FROM medics'))

class PatientCrudOp:
    def __init__(self, app: Flask, db: SQLAlchemy):
        self._app = app
        self._db = db

    def create_patient(self, patient: Patient):
        pass

    def get_patient_id(self, id: str):
        pass

    def get_patient(self, fullname: str):
        pass

    def update_patient(self, id: str):
        pass

    def delete_patient(self, id: str):
        pass

class RecordCrudOp:
    def __init__(self, app: Flask, db: SQLAlchemy):
        self._app = app
        self._db = db

    def create_record(self, record: Record):
        pass

    def get_record(self, id: str):
        pass

    def get_record_id(self, fullname: str):
        pass

    def update_record(self, id: str):
        pass

    def delete_record(self, id: str):
        pass
