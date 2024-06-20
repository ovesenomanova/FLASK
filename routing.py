from flask import Flask, render_template, request, redirect, flash

from data.db_session import GlobalDBManager
from data.sql_request import users_register, users_check_if_exists, users_check_if_username_taken

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template ("index.html", name='Оксана', show_hidden=True)


@app.route('/second_page')
def index_2():
    return render_template ("second_html.html", tel='89279136988')


@app.route('/article/<idd>')
def show_articles(idd):
    return f'Article: {idd}'


@app.route('/hello', methods=['GET'])
def hello_page():
    return render_template('third.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    username = request.form.get("username")
    password = request.form.get("password")

    if users_check_if_username_taken(GlobalDBManager, username):
        flash("Имя пользователя занято!")
        return redirect('/')
    users_register(GlobalDBManager, username, password)
    return redirect('/hello')



