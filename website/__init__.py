from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#loginManager helps manage login related things


db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
# how to  initialize flask refers to the file
    app= Flask(__name__)
    #Secures the cookies and session data
    app.config['SECRET_KEY'] = 'kdakdjdkjdkdksd'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}/'
    #initialize our database 
    db.init_app(app)




    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)
    login_manager = LoginManager()
    #where do flask redirect us when not logged in when login is required
    login_manager.login_view = 'auth.login'
    #telling the login_manager which app we are using
    login_manager.init_app(app)

#Tells flask how we load a user
    @login_manager.user_loader
    def load_user(id):
        #works similar to filter_by except by default it is going to look for primary key
        return User.query.get(int(id))

    return app

def create_database(app):
    with app.app_context():
        if not path.exists('website/' + DB_NAME ):
            db.create_all()
            print('Created Database!')

