from src.database.db import db

class Record(db.Model):

    __tablename__ = 'records'

    id = db.Column('record_id',db.String(100), primary_key = True)
    patient_id = db.Column(db.String(100))
    patient_name = db.Column(db.String(100))
    study = db.Column(db.String(100))
    price = db.Column(db.Integer)
    sponsor = db.Column(db.String(50))
    observations = db.Column(db.String(300))
    date = db.Column(db.String(50))
    images_path = db.Column(db.String(300))
    medic_id = db.Column(db.String(50))
    medic_name = db.Column(db.String(100))
    

