from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
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

        if len(password) <= 8:
            flash(
                'password is to short, password must be greater the 8 charcthers', category='error')
        else:
            flash('Account created!', category='success')

    return render_template('signup.html')
