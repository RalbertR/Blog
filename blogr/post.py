from flask import Blueprint, render_template, url_for, redirect

bp = Blueprint('post', __name__, url_prefix='/post')

@bp.route('/posts')
def posts():
    return redirect(url_for('home.index'))

@bp.route('/create')
def create():
    return 'Pagina de create'

@bp.route('/update')
def update():
    return 'Pagina de update'