import os
import click
from flask.cli import with_appcontext
from faker import Faker

from application import db
from application.models import (
    User,
    Role)

fake = Faker(['it_IT', 'en_US'])


@click.command(name='seed')
@with_appcontext
def seed_db():
    # TODO: fix relationships and add tasks
    # clear_db()
    create_users()
    # create_projects()
    create_tasks()


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


# def create_projects():
#     for _ in range(5):
#         project = Project(
#             title=fake.sentence(nb_words=3),
#             subject=fake.words(nb=1),
#             short_description=fake.sentence(nb_words=8),
#             description=fake.paragraph(nb_sentences=8)
#         )
#         print(
#             f'Dummy Project {project.title}: {project.short_description}')
#         db.session.add(project)
#     db.session.commit()


def create_tasks():
    pass