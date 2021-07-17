from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
    subject = StringField('Body', validators=[DataRequired()])
    submit = SubmitField('Submit')
