"""
Flask
__name__
Python decorator
A little bit of html

A flask project
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about")
def about():
    return "<h1>We are learning flask</h1>"












"""
*args catches any positional arguments
**kwargs catches any keyword arguments
wrapper forwards them into func(*args, **kwargs)

“Code under if __name__ == "__main__" runs only when
the file is executed directly — never when imported.”
"""