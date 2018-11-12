from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class Registrationform(FlaskForm):
    username = StringField('User Name',
                            validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', Validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class Loginform(FlaskForm):
    email = StringField('Email', Validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    rememberme = BooleanField('Remember Me')
    submit = SubmitField('Login') 
