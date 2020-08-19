from flask import render_template, url_for
from app import app


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html', title='Manager')