from flask import Blueprint
from flask import render_template

home_bp = Blueprint('home', __name__, url_prefix='/admin')

@home_bp.route('/')
def index():
    return render_template('home/index.html', message="Hello World!")