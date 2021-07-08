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
    product = relationship('Product', back_populates='user')

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)


class Product(TimestampMixin, db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_photos = relationship('ProductPhoto', back_populates='product')
    user = relationship('User', back_populates='product')


class ProductPhoto(TimestampMixin, db.Model):
    __tablename__ = 'product_photos'

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(), unique=True, nullable=False)
    product = relationship('Product', back_populates='product_photos')
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

