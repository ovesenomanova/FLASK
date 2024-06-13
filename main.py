from flask import Flask, render_template, request, redirect

app = Flask(__name__)

ARTICLES = [
    [0, 'Первая', "Содержание первой статьи"],
    [1, 'Вторая', "Содержание второй статьи"],
    [2, 'Самая интересная', "А тут ничего не писали" ]
    ]

"""
GET - получить с сервера. Например html страницу
POST -отправить на сервер.
"""

@app.route('/', methods=['GET'])
def index():
    return render_template ("index.html", name='Оксана', show_hidden=True, articles=ARTICLES)


@app.route('/second_page')
def index_2():
    return render_template ("second_html.html", tel='89279136988')


@app.route('/article/<idd>')
def show_articles(idd):
    return f'Article: {idd}'


@app.route('/register', methods=['POST', 'GET'])
def register():
    print(request.form.to_dict())
    return redirect('/hello')

@app.route('/hello', methods=['GET'])
def hello_page():
    return render_template('third.html')


app.run()
