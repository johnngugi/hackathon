from flask import Flask, render_template
from read import home, away, scores

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', home=home, away=away, scores=scores)


if __name__ == '__main__':
    app.run(port=4000)
