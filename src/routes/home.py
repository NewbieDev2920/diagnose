from flask import Blueprint, render_template


home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('index.html')

@home_bp.route('/landing')
def entry():
    return render_template('landingpage.html')

