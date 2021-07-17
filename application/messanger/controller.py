import os
from flask_login import current_user
from flask import Flask, jsonify, make_response, redirect, render_template, request, session, url_for
from application.models import Message, User, Ad
from application.messanger.form import MessageForm
from application import db


def get_message(ad_id):
    messages = Message.query.filter(User.id == current_user.id, Ad.id == ad_id)
    return messages


def add_message(ad_id, message):
    new_message = Message(
        ad_id=ad_id,
        subject=message,
        user_id=current_user.id
    )
    db.session.add(new_message)
    db.session.commit()


def main(ad_id):
    ad = Ad.query.get(ad_id)
    if request.method == 'POST':
        print("HERE", flush=True)
        add_message(ad_id=ad_id, message=request.form['subject'])
        redirect(url_for('messenger.main', ad_id=ad_id))
    return render_template('messenger/main.html', messages=get_message(ad_id=ad_id), ad=ad)
