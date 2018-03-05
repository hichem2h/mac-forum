from flask import render_template, flash, redirect, url_for

from app.main import bp

@bp.route('/')
@bp.route('index')
def index():
    return render_template('main/index.html')