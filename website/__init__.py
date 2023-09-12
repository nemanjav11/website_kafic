from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
from flask_login import LoginManager

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore
from flask_security import Security


db = SQLAlchemy()
DB_NAME = "database.db"

PIC_FOLDER=os.path.join('static','pics')


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'd3e9dabcef1bb15908a3c0cd8a7fa4bd8cbb7f2eaf1af14a92c56d7e3a80bd35'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['UPLOAD_FOLDER']= PIC_FOLDER
    db.init_app(app)

   
    from .models import Drink,User,Role
        
    with app.app_context():
        db.create_all()
    
    from .views import views
    

    app.register_blueprint(views, url_prefix='/')
    
    admin=Admin(app)
    admin.add_view(ModelView(Drink,db.session))
    admin.add_view(ModelView(User,db.session))

    # Flask security
    user_datastore= SQLAlchemyUserDatastore(db,User,Role)

    # security= Security (app,user_datastore)
    # user=user_datastore.create_user(email="velickovic.nemanja11@gmail.com", password='tetris4!')
    # db.session.add(user)
    # db.session.commit()
  


    return app

    

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')


