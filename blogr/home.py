from flask import Blueprint

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    return 'Pagina de inicio'

@bp.route('/')
def blog():
    return 'Pagina de blog'