import datetime
import enum

from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from application import db


class Role(enum.Enum):
    admin = 'Admin'
    user = 'User'


class Categories(enum.Enum):
    transport = 'Transport'
    real_estate = 'Real estate'
    electronics = 'Electronics'
    stuff = 'Stuff'
    animals = 'Animals'
    business = 'Business'


class TimestampMixin(object):
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)


class User(UserMixin, TimestampMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    role = db.Column(ENUM(Role), nullable=False)
    ads = relationship('Ad', back_populates='user')
    # messages = relationship('Message', back_populates='sender')
    recipient = relationship("Message", foreign_keys="[Message.recipient_id]", uselist=False, back_populates="recipient")
    sender = relationship("Message", foreign_keys="[Message.sender_id]", uselist=False, back_populates="sender")

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)


class Ad(TimestampMixin, db.Model):
    __tablename__ = 'ads'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(ENUM(Categories), nullable=False)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    ad_photos = relationship('AdPhoto', back_populates='ad')
    messages = relationship('Message', back_populates='ad')
    user = relationship('User', back_populates='ads')

    def __init__(self, title, category, description, user_id):
        self.title = title
        self.category = category
        self.description = description
        self.user_id = user_id


class AdPhoto(TimestampMixin, db.Model):
    __tablename__ = 'ad_photos'

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.Text, nullable=False)
    ad = relationship('Ad', back_populates='ad_photos')
    ad_id = db.Column(db.Integer, db.ForeignKey('ads.id'))

    def __init__(self, link, ad_id):
        self.link = link
        self.ad_id = ad_id


class Message(TimestampMixin, db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.Text)
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    recipient = relationship('User', foreign_keys="[Message.recipient_id]", back_populates="recipient")
    ad_id = db.Column(db.Integer, db.ForeignKey('ads.id'))
    ad = relationship('Ad', back_populates='messages')
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    sender = relationship('User', foreign_keys="[Message.sender_id]", back_populates="sender")
