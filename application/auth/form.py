from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length
)


class SignInForm(FlaskForm):
    """User Log-in Form."""
    login = StringField(
        'Login',
        validators=[
            DataRequired()
        ]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class SignUpForm(FlaskForm):
    """User Sign-up Form."""
    username = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[Length(min=6), Email(message='Enter a valid email.'), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=6, message='Select a stronger password.')])
    confirm = PasswordField('Confirm Your Password', validators=[DataRequired(),
                                                                 EqualTo('password', message='Passwords must match.')])
    submit = SubmitField('Sign Up')
