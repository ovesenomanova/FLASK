from flask import Flask, render_template

app = Flask(__name__)

ARTICLES = [
    [0, 'Первая', "Содержание первой статьи"],
    [1, 'Вторая', "Содержание второй статьи"],
    [2, 'Самая интересная', "А тут ничего не писали" ]
    ]

@app.route('/')
def index():
    return render_template ("index.html", name='Оксана', show_hidden=True, articles=ARTICLES)


@app.route('/second_page')
def index_2():
    return render_template ("second_html.html", tel='89279136988')


@app.route('/article/<idd>')
def show_articles(idd):
    return f'Article: {idd}'


app.run()
