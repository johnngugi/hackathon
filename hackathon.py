from flask import Flask, render_template
from read import home, away, scores, leagues
from scrape import get_date

app = Flask(__name__)


@app.route('/')
def index():
    a = []
    for i in scores:
        a.append(i.encode('utf-8'))
    return render_template('index.html', home=home, away=away, scores=a, leagues=leagues, date=get_date())


if __name__ == '__main__':
    app.run(port=4000)
