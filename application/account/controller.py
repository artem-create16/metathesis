from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user
from application.models import Ad, User


def show_account(user_id):
    user = User.query.get(user_id)
    return render_template('account/main.html', user=user)


def show_my_account():
    ads = current_user.ads
    ads.reverse()
    return render_template('account/main.html', user=current_user, ads=ads)

