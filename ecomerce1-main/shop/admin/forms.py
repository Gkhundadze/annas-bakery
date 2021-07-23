from wtforms import Form, BooleanField, StringField, PasswordField, validators,ValidationError
from flask_wtf import FlaskForm
from .models import User

class RegistrationForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35),validators.DataRequired(),validators.email()])
    password = PasswordField('New Password', [validators.DataRequired(),validators.EqualTo('confirm',
    message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    

    #email  validation
    def validate_email(self,email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError(' This email adress alredy exist!',)
        
    def validate_username(self,username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError(' This username adress alredy exist!',)
    
class LoginForm(FlaskForm):
    email = StringField('Email Address', [validators.Length(min=6, max=35),validators.email()])
    password = PasswordField('New Password', [validators.DataRequired()])





