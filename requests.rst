All about requests
==================

A request is made when a user visits a URL.  There are a few different types (also called methods) of requests.
Here, we will only discuss two types:  ``GET`` and ``POST`` requests.

The ``request`` module must be imported from flask.  You can update the import line in ``application_lulu.py``::

    from flask import Flask,render_template,request

The ``request`` module has an attribute called ``method``, which only has a value if a request is made.  When
the request is made, it takes the value of ``GET`` or ``POST`` (or a few other possible values, but we will are
ignoring them, remember?).

There is some amount of philosophical argument about when to use ``GET`` and when to use ``POST``.  From what I
can tell, ``GET`` definitely should be used when no user-information is being used to produce the page.  (Think
Web 1.0.)  And, ``POST`` should be used when the user is sending information to the server before a page is
returned.  

(Technically, one can receive user input through the ``GET`` request, but it would appear only in
the URL string.  For example, do a Google search and see the URL you are visiting when your search result
returns.  There are question marks, key/value pairs, and other things that define the search.)

GET requests
------------

In the application we have written so far, we have just done a ``GET`` request.  We have asked for a webpage
at ``127.0.0.1:5000/index_lulu``.  Then ``application_lulu.py`` found the correct function to call, and it
returned a webpage (``~/MyFlaskTutorial/templates/userinfo_lulu.html``).

In the function ``index_lulu`` (inside ``application_lulu.py``), the attribute ``request.method`` exists,
and it is equal to ``GET``.

Edit ``application_lulu.py`` and see that this does not change what we have done so far::

    from flask import Flask,render_template
    app_lulu = Flask(__name__)

    @app_lulu.route('/index_lulu',methods=['GET'])
    def index_lulu():
        nquestions=5
	if request.method == 'GET':
            return render_template('userinfo_lulu.html',num=nquestions)
        else:
            return 'request.method was not a GET!'

    if __name__ == "__main__":
        app_lulu.run()
        
Note that we instruct the application which types of requests to accept in the line::

    @app_lulu.route('/index_lulu',methods=['GET'])

I hope that worked for you just as well as it worked for me!  CELEBRATE!  We're almost there!

POST requests
------------

Try entering your name and age in the fields, then click on Submit.  It didn't work, did it?
That's because we did not allow POST requests for the destination ``/index_lulu``.  This can be
remedied by editing the line in ``application_lulu.py`` to::

    @app_lulu.route('/index_lulu',methods=['GET','POST'])

If you try running the application again, when you try to Submit your name and age, you should
get the text we specified above::

    'request.method was not a GET!'

GOOD!  We know what's getting called when.  (At least, I think you should know, based on our
tests so far!)

But, it's not interesting to have the screen tell you it was not a GET request.  We'd rather
the application CALCULATE SOME STUFF or at least RETURN A DIFFERENT PAGE when a POST request
is received.

Let's have it return a page with questions on it.  First, we will need to make the HTML
template, then we will have to instruct the application to use that template.  The next part of 
the tutorial will discuss this.
