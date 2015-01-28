The Grand Finale
================

We want to keep track of questions, and we want the function to show the ``/next_lulu`` to be general.  To do this, let's make a
dictionary with questions (as keys) and tuples of answers (as corresponding values). 

We will have a main function that will determine whether we should go to 1) the next question or 2) the end page (if there are 
no more questions).

We will request ``/next_lulu``with 1) the correct question number and 2) the correct question.  After each question is answered, 
we will "pop" that key/value pair from the dictionary.

We will need to have different processing for GET and POST requests for ``/next_lulu``.  For GET requests, we want to
generate the correct question/answer form, and for the POST requests, we want to write data to file, then redirect
the user to either the next question or the end page.

I hope I haven't lost you!  Let's do it step-by-step, but you won't be able to run anything till the end of this page.

Make the end HTML file
----------------------

Create a file called ``end_lulu.html`` in the templates directory. Make it look like this::
    
    <!doctype html>
    <title>A short quiz</title>
    <link rel=stylesheet type=text/css href='{{ url_for('static',filename='style_lulu.css')}}'>
    <div class=page>
      <h1>A short quiz</h1>
      <div class=metanav>
	<h4>
	  Thank you for participating!
	</h4>
      </div>
    </div>

It's really pretty straightforward.  Nothing fancy here.  But, we need to link to it.

Link to the end page
--------------------

If you don't believe me, you can try out linking to the end page::

    from flask import Flask,render_template,request,redirect
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

    @app_lulu.route('/next_lulu',methods=['POST'])
    def next_lulu():
        return redirect('/usefulfunction_lulu')

    @app_lulu.route('/usefulfunction_lulu',methods=['GET','POST'])
    def usefulfunction_lulu():
        return render_template('end_lulu.html')

    if __name__ == "__main__":
        app_lulu.run(debug=True)

You can try running this.  It will ask you the first question, and when you click Next, it will take you to the End page
we just made.

Now the final program, for real
-------------------------------

Open ``application_lulu.py`` one last time.  Change the contents to look like::

    from flask import Flask,render_template,request,redirect
    app_lulu = Flask(__name__)

    app_lulu.vars={}

    app_lulu.questions={}
    app_lulu.questions['How many eyes do you have?']=('1','2','3')
    app_lulu.questions['Which fruit do you like best?']=('banana','mango','pineapple')
    app_lulu.questions['Do you like cupcakes?']=('yes','no','maybe')

    app_lulu.nquestions=len(app_lulu.questions)
    # should be 3

    @app_lulu.route('/index_lulu',methods=['GET','POST'])
    def index_lulu():
        nquestions=app_lulu.nquestions
        if request.method == 'GET':
            return render_template('userinfo_lulu.html',num=nquestions)
        else:
            # request was a POST
            app_lulu.vars['name'] = request.form['name_lulu']
            app_lulu.vars['age'] = request.form['age_lulu']
            
            f = open('%s_%s.txt'%(app_lulu.vars['name'],app_lulu.vars['age']),'w')
            f.write('Name: %s\n'%(app_lulu.vars['name']))
            f.write('Age: %s\n\n'%(app_lulu.vars['age']))
            f.close()
            
            return redirect('/main_lulu')

    @app_lulu.route('/main_lulu')
    def main_lulu2():
        if len(app_lulu.questions)==0 : return render_template('end_lulu.html')
        return redirect('/next_lulu')

    #####################################
    ## IMPORTANT: I have separated /next_lulu INTO GET AND POST
    ## You can also do this in one function, with If and Else
    ## The attribute that contains GET and POST is: request.method
    #####################################

    @app_lulu.route('/next_lulu',methods=['GET'])
    def next_lulu(): #remember the function name does not need to match the URL
        # for clarity (temp variables)
        n = app_lulu.nquestions - len(app_lulu.questions) + 1
        q = app_lulu.questions.keys()[0] #python indexes at 0
        a1, a2, a3 = app_lulu.questions.values()[0] #this will return the answers corresponding to q

        # save the current question key
        app_lulu.currentq = q

        return render_template('layout_lulu.html',num=n,question=q,ans1=a1,ans2=a2,ans3=a3)

    @app_lulu.route('/next_lulu',methods=['POST'])
    def next_lulu2():  #can't have two functions with the same name
        # Here, we will collect data from the user.
        # Then, we return to the main function, so it can tell us whether to
        # display another question page, or to show the end page.

        f = open('%s_%s.txt'%(app_lulu.vars['name'],app_lulu.vars['age']),'a') #a is for append
        f.write('%s\n'%(app_lulu.currentq))
        f.write('%s\n\n'%(request.form['answer_from_layout_lulu'])) #this was the 'name' on layout.html!
        f.close()

        # Remove question from dictionary
        del app_lulu.questions[app_lulu.currentq]

        return redirect('/main_lulu')

    if __name__ == "__main__":
        app_lulu.run(debug=True)

Try running it.  I HOPE IT WORKS FOR YOU, TOO!  If you look at the code here, you can hopefully follow which
functions are being called as you click through the web application.  

The questions are stored as a dictionary.  The questions are deleted after they are used, and the question
number is determined by the number of key/value pairs in the dictionary.

We have made a ``main_lulu`` function, which determined whether there are any questions left to ask.  If
there are, it calls ``next_lulu`` and displays the form.  If there are no more questions, it shows the
end page.

When a question form page is shown, the user enters information and clicks on ``Next``.  The request is
a POST method type, which calls the appropriate ``next_lulu`` function (``next_lulu2``) (that writes data 
to file).  That function DOES NOT return automatically to another ``next_lulu`` HTML form page.  Instead,
it ``redirects`` to the ``main_lulu`` function, which will tell it whether to return 1) ``end_lulu.html``
or 2) another ``next_lulu`` HTML form page.
