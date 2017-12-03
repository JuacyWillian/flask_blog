from flask import Blueprint, request, render_template, flash

from ..forms import LoginForm, RegisterForm
from ..models import User

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(**request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data


            # todo: authentication

    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(**request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = form.password.data


            # todo: authentication

    return render_template('auth/register.html', form=form)


@auth.route('/password_reset', methods=['GET', 'POST'])
def password_reset():
    pass
