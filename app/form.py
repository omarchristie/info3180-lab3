from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(message='Name is required')])
    email = StringField('email', validators=[InputRequired(message='Email is required')])
    subject = StringField('subject', validators=[InputRequired(message='Subject is requried')])
    message = StringField('message', validators=[InputRequired(message='Message is required')])
    