Linking to the next question
============================

To link one question to the next, we need to tell the server what to do when ``/next_lulu`` is
requested.  This will be a POST request, because we want to take data from the user.

Open ``application_lulu.py`` and add this decorated function::

    @app_lulu.route('/next_lulu',methods=['POST'])
    def next_lulu():  #remember the function name does not need to match the URL                                                              
        return render_template('layout_lulu.html',num=1,question='Which fruit do you like best?',ans1='banana',\
	    ans2='mango',ans3='pineapple')

In case it isn't clear, the whole file ``application_lulu.py`` should now look like::

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

    @app_lulu.route('/next_lulu',methods=['POST'])
    def next_lulu():  #remember the function name does not need to match the URL                                                                                     
        return render_template('layout_lulu.html',num=1,question='Which fruit do you like best?',ans1='banana',\
	    ans2='mango',ans3='pineapple')

    if __name__ == "__main__":
        app_lulu.run()

Try running it.  IT WORKS, RIGHT?  But, when you click on Next after the fruit question, what do you get?  IT'S THE FRUIT QUESTION AGAIN.
How can we fix this?  We need to somehow tell the application to keep track of the questions being asked.  We can make a list of 
questions at the beginning, then iterate through them.

What will come in handy now is to learn about the ``redirect`` function in Flask.  There's also ``url_for``, which you can
Google yourself.  It's not necessary for now.

Redirecting
-----------

The ``redirect`` function in Flask allows a decorated function (a function with ``@app_lulu.route('/index_lulu')`` or similar
preceding the function) to return the HTML template that another function will produce.  Instead of calling ``render_template``
to make an HTML page, we call ``redirect`` and insert the URL for another decorator function, which will call that decorated
function and return the associated HTML code.

Here's an example.  We take the previous code and we just add one more step, which redirects to another function
to give the rendered template::

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

    @app_lulu.route('/usefulfunction_lulu',methods=['POST'])
    def usefulfunction_lulu():
        return render_template('layout_lulu.html',num=1,question='Which fruit do you like best?',ans1='banana',\
	    ans2='mango',ans3='pineapple')

    if __name__ == "__main__":
        app_lulu.run()

I think that's most of the FLASK-ESQUE stuff.  The rest is all PYTHON.  In the next section, we'll put some of this stuff together,
using Python dictionaries to make the question-asking scalable (easier to add more questions), and to automate the process
for many questions.
