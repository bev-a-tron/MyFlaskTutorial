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
        app_lulu.run()

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
    	  <input type='radio' name='answer_lulu' value="1" /> 1
    	  <input type='radio' name='answer_lulu' value="2" /> 2
    	  <input type='radio' name='answer_lulu' value="3" /> 3
    	</p>
    	
    	<p>
    	  <input type='submit' value='Next' />
    	</p>
          </form>
        </h4>  
      </div>
    </div>
        
This is using some HTML skills about forms.  You can look up different types of forms online.
I'm sure Google will tell you.

Now, you probably already realize that we need to refer to this HTML template with two variables,
``num`` (which will be the question number) and ``question`` (which will be the question asked).
The radio button form has a number of choices, but the user can only select one answer.  The
user data can be referred to as ``request.form['answer_lulu']`` in the ``application_lulu.py``
file.

###############
This will be a section on how to dress up the application_lulu.py file.
###############