This is Beverly's Flask tutorial
================================

This tutorial is meant for people who have a good understanding of Python,
but who have never done web programming before.  You should know static HTML, 
but it is not necessary to know about forms, requests, and methods.

I finally "understood" Flask when I realized

- how the different functions are called based on "GET" and "POST" requests
- what a "request" was
- how HTML pages are rendered and returned
- how to use Python as the machinery to decide which function to call

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
        app_lulu.run()

Now, run the code from command line using::

    >> python hello_lulu.py

Running this code will start a server at: 127.0.0.1:5000.  If you visit that 
address in a browser window, you should see a blank screen with text at the 
top right corner, which says "Hello World." 

Note that the ``app_lulu.route('/')`` is showing which code to run (in this 
case, ``hello_world_lulu``) when the URL ``/`` is requested.  (A request is made 
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

Setting up the directory structure
-------------------

Set up your directories like this (put it somewhere, like your home directory)::

    ~/MyFlaskTutorial_lulu
	/static
	/templates

Copy the file ``style_lulu.css`` and put it in the ``static`` directory.  We will not
discuss css style sheets in this Tutorial.  It will just make your app look pretty.  Like
magic.

The ``templates`` directory will hold html files that we will use to construct pages that 
will depend on user input.

In the ``MyFlaskTutorial_lulu`` directory, we will place the main Python program that 
will process requests (on the server side) and return html files to send to the client.

The matching HTML code
----------------------

None of this web app stuff means anything without HTML code.  Let's make a 
simple page, then add a form.  We will use that form to demonstrate HTTP
methods, including `GET` and `POST`.  Don't worry about what they are now.
Let's get some HTML code working first.

Open a file called userinfo_lulu.html, and save it to the ``templates`` directory::

     <!doctype html>
     <title>An example form</title>
     <link rel=stylesheet type=text/css href='{{ url_for('static',filename='style_lulu.css')}}'>
     <div class=page>
       <h1>An example form</h1>
       <div class=metanav>

       <form id='userinfoform' method='post' action='index' >
       <p>
       Name: <input type='text' name='name' />
       </p>
       <p>
       Age: <input type='text' name='age' />
       </p>
       <p>
       <input type='submit' value='Submit' />
       </p>
       </form>
    </div>

