This is Beverly's Flask tutorial
================================

This tutorial is meant for people who have a good understanding of Python,
but who have never done web programming before.  You should know a little
bit of HTML, although it is not necessary to know about forms in HTML,
since I didn't know about forms when I started trying to learn Flask.


Hello world
-----------

Open a file called hello.py.  Type the following::

    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    if __name__ == '__main__':
        app.run()

Run this script using 'python hello.py'.::

