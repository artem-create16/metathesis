import flask
from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user
from typing import Optional

from application.models import User, Role
from application.auth.form import SignUpForm, SignInForm
from application import db, login_manager


@login_manager.user_loader
def load_user(user_id: str) -> Optional[User]:
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flask.flash('You must be logged in to view that page.')
    return redirect(url_for('auth.sign_in'))


def sign_out():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth.sign_in'))


def sign_in():
    """
    Log-in page for registered users.
    GET requests serve Log-in page.
    POST requests validate and redirect user to dashboard.
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = SignInForm()
    if form.validate_on_submit():
        user = User.query.filter(
            (User.email == form.login.data) | (User.username == form.login.data)
        ).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.index'))
        flask.flash('Invalid username/password combination')
        return redirect(url_for('auth.sign_in'))
    return render_template(
        'auth/signin.html',
        form=form,
        title='Sign in'
    )


def sign_up():
    """
    Register page for users.
    GET requests serve Register page.
    POST requests validate and create a new user.
    """

    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = SignUpForm()
    if form.validate_on_submit():
        existing_user = User.query.filter(
            (User.email == form.email.data) | (User.username == form.username.data)
        ).first()
        if existing_user is None:
            user = User(
                username=form.username.data,
                email=form.email.data,
                role=Role.user.name
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('main.index'))
        flask.flash('A user already exists with that username or email address.')
    return render_template(
        'auth/signup.html',
        title='Sign up',
        form=form
    )