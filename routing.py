from flask import Flask, render_template, request, redirect, flash

from data.db_session import GlobalDBManager
from data.sql_request import \
    users_register, \
    users_check_if_exists, \
    users_check_if_username_taken

from auth import AuthUser
from flask_login import current_user, login_user

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    if current_user.is_authenticated:
        return render_template ("index.html", user=current_user)
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")

    if users_check_if_username_taken(GlobalDBManager, username):
        flash("Имя пользователя занято!")
        return redirect('/register')
    users_register(GlobalDBManager, username, password, email)
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get("username")
    password = request.form.get("password")

    user_id = users_check_if_exists(GlobalDBManager, username, password)
    if user_id == 0:
        flash("Неверное имя пользователя или пароль!")
        return redirect('/login')

    user = AuthUser.get( user_id )
    login_user( user )
    return redirect('/')


