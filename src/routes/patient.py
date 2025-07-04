from flask import Blueprint, render_template

patient_bp = Blueprint('patient', __name__)

@patient_bp.route('/patientrecordcatalog')
def patient_record_catalog():
    return render_template('patientRecordCatalog.html')

@patient_bp.route('/focusrecord')
def focus_record():
    return render_template('focusrecord.html')

@patient_bp.route('/getrecords')
def get_records():
    pass

@patient_bp.route('auth')
def auth():
    return render_template('patientLogin.html')

