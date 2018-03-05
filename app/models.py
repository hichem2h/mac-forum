from app import db, login_manager
from datetime import datetime
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    birth_date = db.Column(db.Date())
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(64), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     time_stamp = db.Column(db.DateTime(), default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
