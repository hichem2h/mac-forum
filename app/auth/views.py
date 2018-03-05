from flask import render_template, flash, redirect, url_for

from flask_login import current_user, login_user,logout_user, login_required

from app.auth import bp
from app.auth.forms import LoginForm, RegisterForm
from app.services import UserEditor


@bp.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        error = UserEditor.register_user(form.username.data, form.birth_date.data, form.password.data)

        if not error:
            flash('Registered Successfuly', 'success')
            return redirect(url_for('main.index'))
        else:
            flash(error, 'error')

    return render_template('auth/register.html', form=form)


@bp.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = UserEditor.get_user(form.username.data, form.password.data)
        if user is not None:
            login_user(user, remember=form.remember_me.data)
            flash('Login Successful', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password')

    return render_template('auth/login.html', form = form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
