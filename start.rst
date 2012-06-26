This is Beverly's Flask tutorial
================================

This tutorial is meant for people who have a good understanding of Python,
but who have never done web programming before.  You should know static HTML, 
but it is not necessary to know about forms, requests, and methods.

Some housekeeping 
-----------------

I hate programming tutorials that use function and instance names that look 
like offical names.  There are so many function names and instances in 
tutorials that are totally user-defined.  Basically::

    Name it whatever-you-want, and it will still work!  

Instead of using willy-nilly names like "lulu", I will append "_lulu" to 
the end of logical names, so it will be entirely obvious which names can be 
changed with no penalty.  And, it will give you an idea of what "real"
programmers might use to call a certain function (hint: just drop the "_lulu").
Naming things well is certainly a skill to be desired.

Just realize, if you change the name of the file from hello_lulu.py
to something else, like flufflepuff.py, make sure to mentally make that
change for the rest of the tutorial.


Hello world
-----------

Open a file called hello_lulu.py.  Type the following::

    from flask import Flask
    app_lulu = Flask(__name__)

    @app_lulu.route('/')
    def hello_world_lulu():
        return 'Hello World!'

    if __name__ == '__main__':
        app_lulu.run()::

Now, run the code from command line using::

    >> python hello_lulu.py

