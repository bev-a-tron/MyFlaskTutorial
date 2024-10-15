Linking pages
=============

The next step is to have the POST request

1. store the data
2. take us to the next page

We will pretend like there is only one question for now.  We will add Python magic
later, to tell the application how to know when to stop displaying questions.

Store the data
--------------

The name and age information will be used to write a file called name_age.txt,
which will store responses to the questions in the quiz.  Edit the file called
``application_lulu.py`` to do this::

    from flask import Flask,render_template,request
    app_lulu = Flask(__name__)

    app_lulu.vars={}

    @app_lulu.route('/index_lulu',methods=['GET','POST'])
    def index_lulu():
        nquestions=5
        if request.method == 'GET':
            return render_template('userinfo_lulu.html',num=nquestions)
        else:
            #request was a POST                                                                                                              
            app_lulu.vars['name'] = request.form['name_lulu']
            app_lulu.vars['age'] = request.form['age_lulu']

            f = open('%s_%s.txt'%(app_lulu.vars['name'],app_lulu.vars['age']),'w')
            f.write('Name: %s\n'%(app_lulu.vars['name']))
            f.write('Age: %s\n\n'%(app_lulu.vars['age']))
            f.close()

            return 'request.method was not a GET!'

    if __name__ == "__main__":
        app_lulu.run(port=5001, debug=True)

You can try running this on the server. Enter your name and age, click on Submit.  You
should find a new file saved to your ``~/MyFlaskTutorial`` directory called name_age.txt.

Note that we're making a dictionary called ``vars`` as an attribute of ``app_lulu``.
This will allow us to access those variables in other functions inside ``application_lulu.py``.
In the future, we can store other variables here.

You will also notice that we are accessing a dictionary called ``form`` that is an attribute 
of ``request``.  I mentioned this earlier:  these names are identifiers for the form fields
from the HTML template files.  You can check out ``~/MyFlaskTutorial/templates/userinfo_lulu.html``
to see that we named the name and age fields ``name_lulu`` and ``age_lulu``, respectively.

Writing files is a Python skill.  You can read about this elsewhere, but it's pretty straightforward.

Next, we will turn our attention to making the HTML template to return.

Create the HTML template for questions
--------------------------------------

Open a file called ``layout_lulu.html`` inside the ``~/MyFlaskTutorial/templates/`` directory.
Edit it to look like this::

    <!doctype html>
    <title>A short quiz</title>
    <link rel=stylesheet type=text/css href='{{ url_for('static',filename='style_lulu.css')}}'>
    <div class=page>
      <h1>Question #{{num}}</h1>
      
      <div class=metanav>
	
	{{question}}
	
	<h4>
	  <form id='answerform_lulu' method='post' action='next_lulu' >
	    <p>
	      Answer: <br />
	      <input type='radio' name='answer_from_layout_lulu' value={{ans1}} /> {{ans1}} <br />
	      <input type='radio' name='answer_from_layout_lulu' value={{ans2}} /> {{ans2}} <br />
	      <input type='radio' name='answer_from_layout_lulu' value={{ans3}} /> {{ans3}} <br />
	    </p>
	    
	    <p>
	      <input type='submit' value='NextButton_lulu' />
	    </p>
	  </form>
	</h4>
      </div>
    </div>
    
This is using some HTML skills about forms.  You can look up different types of HTML forms online.
I'm sure Google will tell you.  Some types are: text, password, radio, and checkbox.

Now, you probably already realize that we need to refer to this HTML template with two variables,
``num`` (which will be the question number) and ``question`` (which will be the question asked).
The radio button form has a number of choices, but the user can only select one answer.  The
user data can be referred to as ``request.form['answer_from_layout_lulu']`` in the ``application_lulu.py``
file.

Update the application program
------------------------------

Next, we want to make the ``application_lulu.py`` program render this new HTML template.  Let's do
this for one question first, then we can add more questions.

Open ``application_lulu.py`` and replace the appropriate return line with this.  Try to do it yourself.
If you can't figure it out, the full text is right below::

    return render_template('layout_lulu.html',num=1,question='How many eyes do you have?',ans1='1',\
        ans2='2',ans3='3')

The full ``application_lulu.py`` should look like::

    from flask import Flask,render_template,request
    app_lulu = Flask(__name__)

    app_lulu.vars={}

    @app_lulu.route('/index_lulu',methods=['GET','POST'])
    def index_lulu():
        nquestions=5
        if request.method == 'GET':
            return render_template('userinfo_lulu.html',num=nquestions)
        else:
            #request was a POST                                                                                                                                      
            app_lulu.vars['name'] = request.form['name_lulu']
            app_lulu.vars['age'] = request.form['age_lulu']

            f = open('%s_%s.txt'%(app_lulu.vars['name'],app_lulu.vars['age']),'w')
            f.write('Name: %s\n'%(app_lulu.vars['name']))
            f.write('Age: %s\n\n'%(app_lulu.vars['age']))
            f.close()

            return render_template('layout_lulu.html',num=1,question='How many eyes do you have?',ans1='1',\
	        ans2='2',ans3='3')

    if __name__ == "__main__":
        app_lulu.run(port=5001, debug=True)
        
Try running the application again.  To remind you, navigate to ``~/MyFlaskTutorial`` and type::

    python application_lulu.py

Then go to ``127.0.0.1:5001/index_lulu``.  Enter your information, then click on Submit..

DID YOU GET TO YOUR QUESTION PAGE?  I HOPE SO!

Answer the question, then click on Next.  You should be at the address ``127.0.0.1:5001/next_lulu``
and you should get an error that says::

    Not Found
    The requested URL was not found on the server.
    If you entered the URL manually please check your spelling and try again.

That's because we HAVEN'T TOLD THE SERVER what to do when the URL ``/next_lulu`` is requested. We
told it to go to ``/next_lulu`` in the HTML template (``layout_lulu.html``), where we instructed
the form to take the ``action`` equal to ``/next_lulu``.  The server goes looking for a function
inside ``application_lulu.py`` that is wrapped by the decorator that has ``/next_lulu`` as the
argument.  Look over the code to see that it all links together.

There's no ``@app_lulu.route('/next_lulu`)``, right?  LET'S FIX THAT NEXT.