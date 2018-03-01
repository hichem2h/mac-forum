from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    pin = PasswordField('Pin Code', validators=[DataRequired(), Length(max = 6)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    pin = PasswordField('Pin Code', validators=[DataRequired(), Length( max = 6)])
    pin_repeat = PasswordField('Repeat Pin Code', validators=[DataRequired(), EqualTo(pin)])
    submit = SubmitField('Make Registration')