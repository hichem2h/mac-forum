from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired, EqualTo, Regexp, Length, ValidationError
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Insert your username')])
    password = PasswordField('Password', validators=[DataRequired(message='Insert your password')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(message='Insert a username'),
        Regexp('[\w]+$', message='Username must contain only letters and digits')])

    birth_date = DateField('Date Of Birth',
                           validators=[DataRequired(message='Enter a valid Date (dd/mm/YYYY)')],
                           format='%d/%m/%Y',\
                           render_kw={'placeholder': '20/06/1996 for June 20, 1996'})

    password = PasswordField('Password', validators=[
        DataRequired(message='Insert a password'),
        Length(min = 6, message='Password must be at least 6 characters')])

    password2 = PasswordField('Repeat Password',
                              validators=[DataRequired(message='Confirm password'),
                                          EqualTo('password', message='Passwords don\'t match')])

    submit = SubmitField('Make Registration')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first() is not None:
            raise ValidationError('This user already exists')
