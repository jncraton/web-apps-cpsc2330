from flask import Flask
from flask import send_file, request
from html import escape
import json
import random
from urllib.request import urlopen as get
import sqlite3

app = Flask(__name__)

import random


@app.route("/")
def root():
    return open("36-htmx.html").read()


@app.route("/roll")
def roll():
    """Returns a random dice"""
    return str(random.randint(1, 6))


@app.route("/books")
def book():
    """Returns info about a book"""

    isbn = request.args["isbn"]

    with get(f"https://openlibrary.org/search.json?q=isbn:{isbn}") as res:
        book = json.loads(res.read())["docs"][0]

        return f"""
            <p>Title: {book['title']}</p>
            <p>Author: {book['author_name'][0]}</p>
            <p>Year: {book['first_publish_year']}</p>
            <img src="http://covers.openlibrary.org/b/isbn/{isbn}-L.jpg" alt="Book cover">
        """


@app.route("/pokemon")
def pokemon():
    conn = sqlite3.connect("pokemon.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM pokemon")

    rows = [dict(r) for r in cursor]

    return rows


if __name__ == "__main__":
    app.run(debug=True)
