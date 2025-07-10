from flask import Flask
from blogr import home, auth, post

def create_app():
    app = Flask(__name__)

    #Registro de Vistas
    app.register_blueprint(home.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(post.bp)

    

    return app