from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('inputUsername')
        password = request.form.get('inputPassword')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.user'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash("Username doesn't exist", category='error')
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return 'logout'


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('inputEmail')
        username = request.form.get('inputUsername')
        password = request.form.get('inputPassword')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists!', category='error')
        elif len(password) <= 8:
            flash(
                "password is to short, password must be greater the 8 charcthers", category='error')
        else:
            new_user = User(email=email, password=generate_password_hash(
                password, method='sha256'), username=username)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template('signup.html')
