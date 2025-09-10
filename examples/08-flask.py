from flask import Flask
from flask import send_file, request
app = Flask(__name__)

import random

@app.route('/')
def hello_world():
    return f"Hello, world {random.random()}"

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'

if __name__ == '__main__':
    app.run(debug=True)
