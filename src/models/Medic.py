from src.database.db import db

class Medic(db.Model):

    __tablename__ = 'medics'

    id = db.Column('medic_id', db.String(30), primary_key = True)
    
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(50))
    cellphone = db.Column(db.String(30))
    user = db.Column(db.String(30))
    password = db.Column(db.String(100))
    register_date = db.Column(db.String(100))

    def __repr__(self):
        return f"<Medic id='{self.id}', fullname='{self.fullname}'>"

    def __str__(self):
        return f"<<Medic {self.fullname} (ID: {self.id})>>"
