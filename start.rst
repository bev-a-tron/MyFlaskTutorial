This is Beverly's Flask tutorial
================================

This tutorial is meant for people who have a good understanding of Python,
but who have never done web programming before.  You should know a little
bit of HTML, although it is not necessary to know about forms in HTML,
since I didn't know about forms when I started trying to learn Flask.

Some housekeeping 
-----------------

I hate programming tutorials that use function and instance names that look 
like offical names.  There are so many function names and instances in 
tutorials that are totally user-defined.  Basically::

Name it whatever-you-want, and it will still work!  

Instead of using willy-nilly names like "lulu", I will append "_lulu" to 
the end of logical names, so it will be entirely obvious which names can be 
changed with no penalty.

Just realize, if you change the name of the file from hello_lulu.py
to something else, like flufflepuff.py, make sure to mentally make that
change for the rest of the tutorial.


Hello world
-----------

Open a file called hello.py.  Type the following::

    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    if __name__ == '__main__':
        app.run()::

Now, run the code from command line using::

    >> python hello.py

