from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField   
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User, Post


class Registrationform(FlaskForm):
    username = StringField('User Name',
                            validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username= username.data).first()
        if user:
            raise ValidationError('Taht username is taken, please choose another name.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email= email.data).first()
        if user:
            raise ValidationError('Taht email is taken, please choose another email.')

class Loginform(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    rememberme = BooleanField('Remember Me')
    submit = SubmitField('Login') 
