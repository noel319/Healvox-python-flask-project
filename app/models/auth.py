# Flask modules
from flask_login import UserMixin

# Other modules
from datetime import datetime

# Local modules
from app.extensions import db
from app.utils.models import generate_uuid


class User(db.Model, UserMixin):
    # Specifying the table name
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True )
    uuid = db.Column(db.String(50),
                   primary_key=True,
                   default=generate_uuid,
                   unique=True,
                   nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    adress = db.Column(db.String(255), unique=True)
    sex = db.Column(db.String(50), unique=True)
    birthday = db.Column(db.Date, unique=True)
    role = db.Column(db.String(50), unique=True, nullable=False, default="user")
    is_active = db.Column(db.Boolean, default=False)
    verification_code = db.Column(db.String(6), nullable=True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.name}>"
