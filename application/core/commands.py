import os
import random

import click
from faker import Faker
from flask.cli import with_appcontext

from application import db
from application.models import (
    User,
    Role,
    Ad,
    Categories
)

fake = Faker(['it_IT', 'en_US'])


@click.command(name='seed')
@with_appcontext
def seed_db():
    create_users()
    create_ads()


def create_users():
    admin = User(username='admin',
                 email=os.environ['ADMIN_EMAIL'],
                 role=Role.admin)
    admin.set_password('123123')
    db.session.add(admin)
    for _ in range(3):
        user = User(username=fake.user_name(),
                    email=fake.free_email(),
                    role=Role.user)
        user.set_password('123123')
        print(
            f'Dummy user:  {user.username} {user.email}')
        db.session.add(user)
    db.session.commit()


def create_ads():
    admin = User.query.filter(User.username == 'admin').first()
    for _ in range(5):
        ad = Ad(
            title=fake.sentence(nb_words=3),
            category=random.choice([i.name for i in Categories]),
            description=fake.sentence(nb_words=8),
            user_id=admin.id
        )
        print(
            f'Dummy Ad {ad.title}: {ad.description}')
        db.session.add(ad)
    db.session.commit()



