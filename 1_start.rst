This is Beverly's Flask tutorial
================================

This tutorial is meant for people who have a good understanding of Python,
but who have never done web programming before.  You should know static HTML, 
but it is not necessary to know about forms, requests, and methods.

Since any application is nothing other than a way to represent data one should note that there is
there is subtle difference between a web application and a desktop application, a desktop application
normally is designed to be used by a single person, a web application could be used by millions of people
at that same time.

A Desktop application has either a GUI interface or the commandline interface. Web applications provide access
ideally on port 80, in that way you don't need a 'client' to access the service that is running on port 80. 
With flask however you have the freedom to choose the port number, I never had done web programming using a 
framework before Flask, so it was difficult to understand the basic ideas, in PHP we save the .php files in
the 'www' folder, but modern frameworks do not need to place all the projects in one root folder (the www one), 
the main difference between modern frameworks is there is a modular approach in designing the application, 
normally in PHP you write code in .php files and link them to each other from various files.

But there is a problem in PHP, giving sexy links (the ones like Quora.com), it is quite difficult to give 
cute links that are easy to remember, with Flask you get a wonderful way to program web applications.

You create 'links' and then associate with the links a function, you can associate python functions with each 'link'
and that function is executed when the link is requested [with GET or POST, for now the difference shouldn't matter at all],
there are static assets like HTML pages, CSS or JS scripts. The HTML pages have python markup inside them.

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

A Quick Note about Debug Mode
-----------------------------
In this tutorial, you'll be running your app in Debug Mode.  This is very helpful
for you - it means that if the server hits an error, it will give you a detailed 
message instead of just "500 - Internal Server Error" or something similarly 
non-obvious.  However, it's important to note that debug mode is HIGHLY 
INSECURE, and should absolutely never be used on production machines.  If that 
doesn't mean much to you, don't worry about it - you won't be running on 
production machines in this tutorial.  

Hello world
-----------

Open a file called hello_lulu.py.  Type the following::

    from flask import Flask
    app_lulu = Flask(__name__)

    @app_lulu.route('/hello_lulu2')
    def hello_world_lulu():
    	# this is a comment, just like in Python
	# note that the function name and the route argument
	# do not need to be the same.
        return 'Hello World!'

    if __name__ == '__main__':
        app_lulu.run(debug=True)

Now, run the code from command line using::

    >> python hello_lulu.py

Running this code will start a server at: 127.0.0.1:5000/hello_lulu2.  If you 
visit that address in a browser window, you should see a blank screen with 
text at the top left corner, which says "Hello World!" 

Note that the ``@app_lulu.route('/hello_lulu2')`` is showing which code to run (in this 
case, ``hello_world_lulu``) when the URL ``/hello_lulu2`` is requested.  (A request is made 
when the URL is visited.)

When the URL is visited, the code is run, and a string is returned.  The 
string is the HTML code for the page.  Since HTML does not parse white space,
one long string will translate to an HTML page easily.

Short note on browsers
----------------------

127.0.0.1 is Home, or your own computer.  5000 is the port number.  Flask
puts the server on Port 5000 as the default. I'm not going to talk a lot 
about this (actually I'm not going to talk at all about this), because you 
can play with this on your own later.
