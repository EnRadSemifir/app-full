from flask_sqlalchemy import SQLAlchemy
from models.user import User

db = SQLAlchemy()


def get_users():
    return User.query.all()


def get_user_by_name(user_name):
    return User.query.filter_by(lastname=user_name).all()


def create_user(user):
    db.session.add(user)
    db.session.commit()
    return user


def update_user(user_id, user):
    user_data = User.query.get(user_id)
    user_data.lastname = user.lastname
    user_data.firstname = user.firstname
    user_data.birth = user.birth
    user_data.email = user.email
    user_data.login = user.login
    user_data.password = user.password
    db.session.commit()
    return user


def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
