from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class AdForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Category', validators=[DataRequired()], choices=[])
    description = TextAreaField('Description')
    connection = TextAreaField('Connection', validators=[DataRequired()])
    submit = SubmitField('Sign In')
