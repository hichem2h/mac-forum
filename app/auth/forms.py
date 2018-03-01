from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Insert your username')])
    pin = PasswordField('Pin Code', validators=[DataRequired(message='Insert your pin code'), Length(min = 6, max = 6, message='Pin must be 6 digits long')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Insert a username')])
    birth_date = DateField('Date Of Birth', validators=[DataRequired(message='Enter a valid Date (dd/mm/YYYY)')], format='%d/%m/%Y',\
                           render_kw={'placeholder': '20/06/1996 for June 20, 1996'})
    pin = PasswordField('Pin Code', validators=[DataRequired(message='Insert a pin code'), Length(min = 6, max = 6, message='Pin must be 6 digits long')])
    pin_repeat = PasswordField('Repeat Pin Code', validators=[DataRequired(message='Confirm pin code'), EqualTo('pin', message='Pin codes don\'t match')])
    submit = SubmitField('Make Registration')