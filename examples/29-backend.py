from flask import Flask
from flask import send_file, request
from html import escape
import json
import random

app = Flask(__name__)

import random

@app.route('/')
def root():
    return open('29-json.html').read()

@app.route('/rolls')
def greet():
    """ Returns 10 random dice rolls """
    return json.dumps([random.randint(1, 6) for _ in range(10)])
    
if __name__ == '__main__':
    app.run(debug=True)
