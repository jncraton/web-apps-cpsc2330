from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route('/')
def index():
    return f"""
        <figure>
        <img src="{url_for('static', filename='sunset.jpg')}" alt="sunset" height="254">
        <figcaption>A Martian sunset</figcaption>
        </figure>
    """

if __name__ == '__main__':
    app.run(debug=True)
