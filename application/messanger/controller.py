from flask_login import current_user
from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import db
from application.models import Message, Ad
from sqlalchemy import and_, func


def get_message(ad_id, sender_id):
    messages = Message.query.filter(Message.ad_id == ad_id, Message.sender_id == sender_id)
    return messages


def add_message(ad_id, message):
    new_message = Message(
        ad_id=ad_id,
        subject=message,
        sender_id=current_user.id
    )
    db.session.add(new_message)
    db.session.commit()


def main(ad_id):
    ad = Ad.query.get(ad_id)
    if request.method == 'POST':
        add_message(ad_id=ad_id, message=request.form['subject'])
        redirect(url_for('messenger.main', ad_id=ad_id))
    return render_template('messenger/main.html',
                           messages=get_message(ad_id=ad_id,
                                                sender_id=current_user.id), ad=ad)


def my_messages():
    # Если владелец поста current_user и пост имеет сообщения
    # + Все посты, где отправитель сообщения - current_user
    messages = Message.query.filter(and_(Ad.user_id == current_user.id, Ad.messages is not None,
                                         Ad.messages.user_id == current_user)).all()

    # m = Ad.query.join(Message).filter_by(
    #     Ad.user_id == current_user.id, func.count(Ad.messages) > 0
    # ).group_by(Ad.id).all()
    # print(m, flush=True)

    # m1 = Ad.query.filter(
    #     Ad.user_id == current_user.id, func.count(Ad.messages) > 0
    # ).group_by(Ad.id).all()
    #
    # m2 = db.session.query(Ad).join(Message).filter(
    #     Ad.user_id == current_user.id, func.count(Ad.messages) > 0
    # ).all()
    #
    # print(m1, flush=True)

    return render_template('messenger/my_messages.html', ads=m1)

