import random
from flask import Flask, request, render_template, jsonify


app = Flask(__name__, static_url_path="")


@app.route('/')
def index():
    """Return the main page."""
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Return a random prediction."""
    return jsonify({'probability': random.random()})

