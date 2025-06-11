#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#TODO: agregar correctamente focusrecord.html

from flask import Flask, render_template
from database.db import db
from routes.medic import medic_bp
from routes.patient import patient_bp
from routes.home import home_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.sqlite3'
app.debug = True

db.init_app(app)

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

