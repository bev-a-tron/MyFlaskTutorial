Setting up the quiz application
===============================

To set up the application, we will make the directory structure, copy over a CSS style sheet, and build an HTML form.

Setting up the directory structure
----------------------------------

Set up your directories like this (put it somewhere, like your home directory)::

    ~/MyFlaskTutorial_lulu
        /static
        /templates

Copy the file ``style_lulu.css`` (find it in the Github repository, in the static directory) and put it in the ``static`` directory.  We will not
discuss CSS style sheets in this tutorial.  It will just make your app look pretty.  Like
magic.

The ``templates`` directory will hold HTML files that we will use to construct pages that
will depend on user input.

In the ``MyFlaskTutorial_lulu`` directory, we will place the main Python program that
will process requests (on the server side) and return html files to send to the client.


An HTML form
------------

None of this web app stuff means anything without HTML code.  Let's make a
simple page, then add a form.  We will use that form to demonstrate HTTP
methods, including `GET` and `POST`.  Don't worry about what they are now.
Let's get some HTML code working first.

Open a file called ``userinfo_lulu.html``, and save it to the ``templates`` directory::

    <!doctype html>
    <title>A short quiz</title>
    <link rel=stylesheet type=text/css href='{{ url_for('static',filename='style_lulu.css')}}'>
    <div class=page>
      <h1>A short quiz</h1>
      <div class=metanav>
        
        <h4>                                                                                    
          You will be asked a series of questions.                                                
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
    	<input type='submit' value='Submit_lulu' />
          </p>
        </form>
        
      </div>
    </div>

Once the HTML file is written, you can view it in a web browser.  You can do this from command line.  For example::

     open -a /Applications/Google\ Chrome.app/ userinfo_lulu.html

Take a look at the url_for method in the link tag. The url_for method will help figure out the css filepath.
    
    url_for('static',filename='style_lulu.css')

For funsies, you can try entering data to the form, then clicking on Submit.  You might get an error that looks like this::

    No webpage was found for the web address: file://localhost/Users/administrator/MyFlaskTutorial/templates/index_lulu
    Error 6 (net::ERR_FILE_NOT_FOUND): The file or directory could not be found.

In the next part of the tutorial, we will build the backend that will generate the page that cannot currently be found.