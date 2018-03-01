from flask import render_template, flash
from app.auth import bp
from app.auth.forms import LoginForm, RegisterForm

@bp.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Username {form.username.data} tried to connect')

    return render_template('auth/login.html', form = form)

@bp.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('auth/register.html', form = form)