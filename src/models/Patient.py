from src.database.db import db
import datetime

class Patient(db.Model):

    __tablename__ = 'patients'

    id = db.Column('patient_id', db.String(30), primary_key = True)
    idType = db.Column(db.String(5))
    fullname = db.Column(db.String(100))
    birthdate = db.Column(db.String(50))
    cellphone = db.Column(db.String(30))
    email = db.Column(db.String(50))
    user = db.Column(db.String(50))
    password = db.Column(db.String(50))
    register_date = db.Column(db.String(50))
    
