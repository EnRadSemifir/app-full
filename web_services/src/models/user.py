from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String)
    firstname = db.Column(db.String)
    birth = db.Column(db.String)
    email = db.Column(db.String)
    login = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, lastname,firstname,birth,email,login,password):
        self.lastname=lastname
        self.firstname=firstname
        self.birth=birth
        self.email=email
        self.login=login
        self.password=password

    def __repr__(self):
        return f'<User id:{self.id} lastname:{self.lastname} firstname:{self.firstname} birth:{self.birth} email:{self.email} login:{self.login} password:{self.password}>'
