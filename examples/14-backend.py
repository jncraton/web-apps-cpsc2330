from flask import Flask
from flask import send_file, request
from html import escape

app = Flask(__name__)

import random

@app.route('/')
def root():
    template = open('14-dice-roller.html').read()

    max_val = int(request.args.get("size", 6))
    value = random.randint(1, max_val)
    
    return template.replace("{result}", str(value))

@app.route('/greet')
def greet():
    return f"Hello, {escape(request.args['name'])}"

if __name__ == '__main__':
    app.run(debug=True)
