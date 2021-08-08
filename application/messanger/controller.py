from flask import redirect, render_template, request, url_for
from flask_login import current_user
from sqlalchemy import or_

from application import db
from application.models import Message, Ad


def get_message(ad_id, interlocutor_id):
    messages = Message.query.filter(Message.ad_id == ad_id
                                    , Message.interlocutor_id == interlocutor_id)
    return messages


def add_message(ad_id, message):
    ad = Ad.query.get(ad_id)
    new_message = Message(
        ad_id=ad_id,
        subject=message,
        interlocutor_id=current_user.id,
        user_id=ad.user_id
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
                                                interlocutor_id=current_user.id), ad=ad)


def my_messages():
    """
    Если владелец поста current_user и пост имеет сообщения
    (на каждого отправителя к моему посту новый диалог,
    на одного и того же отправителя на разные посты новый диалог)

    + Все посты, где отправитель сообщения - current_user
    """
    m = db.session.query(
        Message.ad_id,
        Message.id,
        Message.interlocutor_id,
        Message.user_id,
        Message.subject
    ).filter(
        or_(
            Message.interlocutor_id == current_user.id,
            Message.user_id == current_user.id
        )
    ).group_by(
        Message.id, Message.ad_id
    ).all()
    # m_dict = {}
    # for message in m:
    #     if message.ad.id not in m_dict:
    #         m_dict[message.ad.id] = [message]
    #     else:
    #         m_dict[message.ad.id].append(message)
    # print(m_dict)
    print('All message for current_user ->', m, flush=True)
    # return render_template('messenger/my_messages.html', m=m_dict)
    return 'ALL IS OK'
