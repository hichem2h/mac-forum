from flask import render_template, flash, redirect, url_for

from app.auth import bp
from app.auth.forms import LoginForm, RegisterForm

from app.services import UserEditor


@bp.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Username {form.username.data} tried to connect')

    return render_template('auth/login.html', form = form)


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