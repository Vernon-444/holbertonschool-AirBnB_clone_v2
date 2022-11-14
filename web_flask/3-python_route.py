#!/usr/bin/python3
"""
Script that starts a Flask web application listening on 0.0.0.0:5000
Route /: display "Hello HBNB!"
Route /hbnb: display "HBNB"
Route /c/<text>: display "C" followed by the value of text
Route /python/<text>: display "Python"l followd by the value of text
The default value of text is is cool
Must use option 'strict_slashes=False'
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_HBNB():
    """
    Prints Hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    prints HBNB
    """
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """
    prints C followed by value of text
    """
    text = text.replace("_", " ")
    return ("C {}".format(text))


@app.route("/python")
def py_is_cool():
    """
    prints Python is cool
    """
    return("Python is cool")


@app.route("/python/<text>")
def py_text(text):
    """
    prints Python followed by the value of text
    default value of text is "is cool"
    """
    text = text.replace("_", " ")
    return("Python {}".format(text))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
