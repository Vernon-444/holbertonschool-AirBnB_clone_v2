#!/usr/bin/python3
"""
Script that starts a Flask web application listening on 0.0.0.0:5000
Route /: display "Hello HBNB!"
Route /hbnb: display "HBNB"
Route /c/<text>: display "C" followed by the value of text
Route /python/<text>: display "Python"l followd by the value of text
The default value of text is is cool
Must use option 'strict_slashes=False'
Route /number/<n>
"""
from flask import Flask, render_template


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
def py_text(text="is cool"):
    """
    prints Python followed by the value of text
    default value of text is "is cool"
    """
    text = text.replace("_", " ")
    return("Python {}".format(text))


@app.route("/number/<int:n>")
def print_int(n):
    """
    If n is an INT, prints <n> is a number
    """
    return("{} is a number".format(n))


@app.route("/number_template/<int:n>")
def html_int(n):
    """
    Displays an HTML page only if n is an integer
    H1 tag: Number: <n> inside tag BODY
    """
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>")
def html_even_odd(n):
    """
    Displays an HTML page only if n is an integer
    """
    if ((n % 2) == 0):
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    return render_template('6-number_odd_or_even.html', number=n,
                           even_or_odd=even_or_odd)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
