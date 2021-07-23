from wtforms import Form,StringField, TextAreaField, PasswordField, SubmitField,validators,ValidationError
from flask_wtf.file import FileField,FileAllowed,FileField
from flask_wtf import FlaskForm
from .model import Register

class CustomerRegistrationForm(FlaskForm):
    name =StringField('Name: ')
    username = StringField('Username: ',[validators.DataRequired()])
    email = StringField('Email ',[validators.Email(),validators.DataRequired()])
    password = PasswordField('Password ',[validators.DataRequired(),validators.EqualTo('confirm',message=' Both password must match! '),validators.Length(min=5, max=35),])
    confirm= PasswordField('Repeat Password: ',[validators.DataRequired()])
    country= StringField('Country: ',[validators.DataRequired()])
    city= StringField('City: ',[validators.DataRequired()])
    # state= StringField('City: ',[validators.DataRequired()])
    contact= StringField('Contact: ',[validators.DataRequired()])
    address=StringField('Address: ',[validators.DataRequired()])
    zipcode= StringField('Zip code: ',[validators.DataRequired()])

    profile=FileField('Profile', validators=[FileAllowed(['jpg','png','jpeg','gif'],'Image only please')])
    submit=SubmitField('Register')
    

    #validation username
    def validate_username(self,username):
        if Register.query.filter_by(username=username.data).first():
            raise ValidationError('This name alredy exist!')

    #email  validation
    def validate_email(self,email):
        if Register.query.filter_by(email=email.data).first():
            raise ValidationError(' This email adress alredy exist!',)

#Customer loginform
class CustomerLoginForm(FlaskForm):
    email=StringField('Email: ' ,[validators.Email(),validators.DataRequired()])
    password=StringField('Password: ',[validators.DataRequired()])

class CustomerEditInfo(FlaskForm):
    name =StringField('Name: ')
    username = StringField('Username: ',[validators.DataRequired()])
    email = StringField('Email ',[validators.Email(),validators.DataRequired()])
    password = PasswordField('Password ',[validators.DataRequired(),validators.EqualTo('confirm',message=' Both password must match! '),validators.Length(min=5, max=35),])
    confirm= PasswordField('Repeat Password: ',[validators.DataRequired()])
    contact= StringField('Contact: ',[validators.DataRequired()])
    address=StringField('Address: ',[validators.DataRequired()])
    profile=FileField('Profile Img', validators=[FileAllowed(['jpg','png','jpeg','gif'],'Image only please')])
