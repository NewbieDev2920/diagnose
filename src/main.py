#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#TODO: agregar correctamente focusrecord.html

from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

from sqlalchemy import text
#from database.db import db
from routes.medic import medic_bp
from routes.patient import patient_bp
from routes.home import home_bp
from database.db import db
from config import *
from models.Medic import Medic
from models.Patient import Patient
from models.Record import Record

#%%% DATABSE CONFIG AND CONNECTION
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)
with app.app_context():
    db.session.execute(text(SQLITE_MANUAL_MEDIC_TABLE_CREATION))
    print(db.session.get(Medic,'1'))

#%%%

app.register_blueprint(medic_bp, url_prefix='/medic')
app.register_blueprint(patient_bp, url_prefix='/patient')
app.register_blueprint(home_bp,url_prefix='/home')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

@app.route('/401')
def debug_401():
    return render_template('401.html')

@app.route('/503')
def debug_503():
    return render_template('503.html')

if __name__ == '__main__':
    app.run()

