from flask import redirect, render_template, request, url_for
from flask_login import current_user
from sqlalchemy import or_
from application import db
from application.models import Message, Ad


def get_message(ad_id, sender_id):
    messages = Message.query.filter(Message.ad_id == ad_id, Message.sender_id == sender_id)
    return messages


def add_message(ad_id, message):
    ad = Ad.query.get(ad_id)
    new_message = Message(
        ad_id=ad_id,
        subject=message,
        sender_id=current_user.id,
        recipient_id=ad.user_id
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
    m = db.session.query(Message).filter(or_(
        Message.sender_id == current_user.id,
        Message.recipient_id == current_user.id
    )).order_by(
        Message.created_at.desc()
    ).all()
    m_dict = {}
    for message in m:
        if message.ad.id not in m_dict:
            m_dict[message.ad.id] = [message]
        else:
            m_dict[message.ad.id].append(message)
    print(m_dict)
    print('All message for current_user ->', m, flush=True)
    return render_template('messenger/my_messages.html', m=m)
