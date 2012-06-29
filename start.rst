This is Beverly's Flask tutorial
================================

This tutorial is meant for people who have a good understanding of Python,
but who have never done web programming before.  You should know static HTML, 
but it is not necessary to know about forms, requests, and methods.

I finally "understood" Flask when I realized

- how the different functions are called based on "GET" and "POST" requests
- what a "request" was
- how HTML pages are rendered and returned
- how to use Python as the machinery to decide which function to call (and thus
  which HTML template to return)

After a short visit with a simple "Hello World" application, we will build a quiz
application that will demonstrate "GET" and "POST" requests, rendering HTML templates,
and redirecting to other functions that will render the appropriate HTML 
templates.  User input will determine the HTML pages that are returned, and 
the data will be written to a text file on the server side.

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

    @app_lulu.route('/hello_lulu2')
    def hello_world_lulu():
        return 'Hello World!'

    if __name__ == '__main__':
        app_lulu.run()

Now, run the code from command line using::

    >> python hello_lulu.py

Running this code will start a server at: 127.0.0.1:5000/hello_lulu2.  If you 
visit that address in a browser window, you should see a blank screen with 
text at the top left corner, which says "Hello World." 

Note that the ``app_lulu.route('/hello_lulu2')`` is showing which code to run (in this 
case, ``hello_world_lulu``) when the URL ``/hello_lulu2`` is requested.  (A request is made 
when the URL is visited.)

When the URL is visited, the code is run, and a string is returned.  The 
string is the HTML code for the page.  Since HTML does not parse white space,
one long string will translate to an HTML page easily.

Short note on browsers
----------------------

127.0.0.1 is Home, or your own computer.  5000 is the port number.  Flask
puts the server on Port 5000 as the defualt. I'm not going to talk a lot 
about this (actually I'm not going to talk at all about this), because you 
can play with this on your own later.