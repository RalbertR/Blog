from flask import Blueprint, render_template

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/')
def blog():
    return render_template('blog.html')