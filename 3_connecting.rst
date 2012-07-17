Connecting an application with HTML
===================================

Copy ``hello_lulu.py``.  Call the new file ``application_lulu.py``.  We will edit this file 
to produce a web application that will display the HTML form when the specified URL is
accessed.


Making the application
----------------------

Inside ``application_lulu.py``, edit the file to look like this::

       from flask import Flask,render_template
       app_lulu = Flask(__name__)
       
       @app_lulu.route('/index_lulu')
       def index_lulu():
           return render_template('userinfo_lulu.html')

       if __name__ == "__main__":
           app_lulu.run()

You can try running it now with::

    python application_lulu.py

Open a browser window and go to::
    
    127.0.0.1:5000/index_lulu

WOW!  It looks PRETTY!  Yes, that's the ``style_lulu.css`` that we added to the 
``~/MyFlaskTutorial/static directory``.  Don't worry about it for now.

You should see the form we just made, with the user information and Submit buttom. 
``Render_template`` will look for that HTML template in the ``~/MyFlaskTutorial/templates``
directory.  That's why we put it there!

In the ``hello world`` example, we saw that these functions must return text
(HTML code).  The ``render_template`` function will return text, and 
HTML text in fact!

Passing variables to HTML files
-------------------------------

You can pass variables to the output HTML through the ``render_template`` function.
For example, we may want to tell the user how many questions we're going to ask.

To do this, edit the ``application_lulu.py`` file::

       from flask import Flask,render_template
       app_lulu = Flask(__name__)
       
       @app_lulu.route('/index_lulu')
       def index_lulu():
           nquestions=5
           return render_template('userinfo_lulu.html',num=nquestions)

       if __name__ == "__main__":
           app_lulu.run()

You also need to edit the HTML file to tell it to expect the variable
``num`` and to tell it what to do with that information.

Open and edit the file ``~/MyFlaskTutorial/templates/userinfo_lulu.html``::

    <!doctype html>
    <title>A short quiz</title>
    <link rel=stylesheet type=text/css href='{{ url_for('static',filename='style_lulu.css')}}'>
    <div class=page>
      <h1>A short quiz</h1>
      <div class=metanav>
        <h4>                                                                                                                
          You will be asked {{num}} questions.
          Please answer them to the best of your ability.                                                                     
        </h4>
        
        <form id='userinfoform_lulu' method='post' action='index_lulu' >
          <p>
    	Name: <input type='text' name='name_lulu' />
          </p>
          <p>
    	Age: <input type='text' name='age_lulu' />
          </p>
          <p>
    	<input type='submit' value='Submit' />
          </p>
        </form>
        
      </div>
    </div>
        
Isn't that awesome?  We can pass variables from our backend to the rendered HTML page.  

While we're here, take a look at the option called ``action`` in the ``form`` tag.  Do you remember 
the error we got when we tried to click Submit?  It told us it couldn't find a page called ``index_lulu``,
right?  Here's where we told it to look.  If you change this to ``index_tutu``, the error will say::
   
    No webpage was found for the web address: file://localhost/Users/administrator/MyFlaskTutorial/templates/index_tutu
    Error 6 (net::ERR_FILE_NOT_FOUND): The file or directory could not be found.

Where is it looking for this file?  It's actually looking in application_lulu.py, trying to find a URL
among the arguments to the ``@app_lulu.route()`` decorators.  If the URL is found, it will carry out the
function that the decorator decorates (the function immediately below the ``@app_lulu.route()`` line).
That function will return text (HTML code), and that is the page that will be loaded.  

For the time being, in ``application_lulu.py``, we have created a decorated function::

    @app_lulu.route('/index_lulu')
    def index_lulu():
    	...

So, the webpage CAN be found at ``127.0.0.1:5000/index_lulu``, and we are telling the client that the 
webpage to be returned (when Submit is clicked) is ``userinfo_lulu.html``, which can be found in 
the ``~/MyFlaskTutorial/templates``

It works so far!

Preparing to learn about POST requests
------------------------------------------

You might also be curious about these options called ``name`` in two of the ``input`` tags in the ``form``. 
These are the identifiers for their respective user-input fields in the form (which we have also named,
``userinfoform_lulu``).  Here, we have called the ``name`` field ``name_lulu`` and we have called the ``age``
field ``age_lulu``.

We will need these identifiers as we progress to the next step:  understanding ``POST`` requests.