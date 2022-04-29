# v-1.0
from project import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=7777)