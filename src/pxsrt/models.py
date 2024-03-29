from pxsrt import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    profpic = db.Column(db.String(20), nullable=False, default='default.jpg')
    uploads = db.relationship('Upload', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.id}', " \
               f"'{self.username}', " \
               f"'{self.email}', " \
               f"'{self.profpic}')"


class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    filename = db.Column(db.String(20), unique=False, nullable=False)
    t_filename = db.Column(db.String(20), unique=True, nullable=True)
    s_filename = db.Column(db.String(20), unique=True, nullable=True)

    def __repr__(self):
        return f"Upload('{self.filename}')"
