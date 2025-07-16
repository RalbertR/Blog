from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    
    # Importar blueprints después de configurar db
    from blogr import home, auth, post
    
    #Registro de Vistas
    app.register_blueprint(home.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(post.bp)

    from .models import User, Post

    with app.app_context():
        db.create_all()

    return app