from flask_login import UserMixin
from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash

class Pitch(db.Model):

    __tablename__ = 'pitchs'

    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String)
    pitch = db.Column(db.String)
    user_id =db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref = 'pitch', lazy = 'dynamic')



    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls,cat):
        pitch = Pitch.query.filter_by(category=cat).all()
        return pitch

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))  # to store passwords
    pitch = db.relationship('Pitch', backref = 'username', lazy = 'dynamic')
    comments = db.relationship('Comment',backref = 'username', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)



    def __repr__(self):
        return f' {self.username}'

class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitchs_id = db.Column(db.Integer, db.ForeignKey("pitchs.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls,id):
        comment = Comment.query.filter_by(pitchs_id=id).all()
        return comment

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
