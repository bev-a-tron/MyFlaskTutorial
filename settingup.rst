Setting up the quiz application
===============================

To set up the application, we will make the directory structure, copy over a CSS style sheet, and build an HTML form.

Setting up the directory structure
----------------------------------

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


An HTML form
------------

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

