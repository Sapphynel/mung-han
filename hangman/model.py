import random
import os

from hangman.extensions import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

def random_pk():
    return random.randint(1e9, 1e10)

def random_word():
    path = os.path.abspath("hangman/words.txt")
    words = [line.strip() for line in open(path)]
    return random.choice(words).lower()

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    games = db.relationship('Game', backref="player", lazy="dynamic")
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
      self.password_hash = generate_password_hash(password)

    def check_password(self, password):
      return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class Game(db.Model):
    pk = db.Column(db.Integer, primary_key=True, default=random_pk)
    word = db.Column(db.String(50), default=random_word)
    tried = db.Column(db.String(50), default='')
    player_id = db.Column(db.String(50), db.ForeignKey("user.id"))

    @property
    def errors(self):
        return ''.join(set(self.tried) - set(self.word))

    @property
    def current(self):
        return ''.join([c if c in self.tried else '_' for c in self.word])

    def try_letter(self, letter):
        if not self.finished and letter not in self.tried:
            self.tried += letter
            db.session.commit()

    # Game status

    @property
    def won(self):
        return self.current == self.word

    @property
    def lost(self):
        return len(self.errors) == 10

    @property
    def finished(self):
        return self.won or self.lost
