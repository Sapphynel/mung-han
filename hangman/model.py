from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    pass

class Game(db.Model):
    pass

class Words(db.Model):
    pass
