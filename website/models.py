from . import db
from flask_login import UserMixin
from flask_security import RoleMixin

from sqlalchemy.sql import func

roles_users= db.Table('roles_users', db.Column('user_id',db.Integer,
                                               db.ForeignKey('user.id')),
                      db.Column('role_id',db.Integer,
                                db.ForeignKey('role.id')))
                        

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100),unique=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    roles = db.relationship('Role',secondary=roles_users, backref=db.backref('users'),lazy='dynamic')
    active=db.Column(db.Boolean)
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type=db.Column(db.String(20))
    head= db.Column(db.String(50),unique=True)
    description= db.Column(db.String(50))
    price= db.Column(db.Integer)

