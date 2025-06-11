from flask import Blueprint, render_template

medic_bp = Blueprint('medic',__name__)

@medic_bp.route('/getrecordsmediclevel')
def get_records_medic_level():
    pass

@medic_bp.route('/catalog')
def catalog():
    return render_template('catalog.html')

@medic_bp.route('/createrecord')
def create_record():
    return render_template('createRecord.html')

@medic_bp.route('/create_patient')
def create_patient():
    return render_template('createPatient.html')

@medic_bp.route('/newrecord')
def new_record():
    return 'lol'

@medic_bp.route('/newpatient')
def new_patient():
    pass

@medic_bp.route('searchpatient')
def search_patient():
    pass

@medic_bp.route('/auth')
def medic_auth():
    return render_template('medicLogin.html')

