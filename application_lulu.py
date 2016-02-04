from flask import Flask,render_template,request,redirect
app_lulu = Flask(__name__)

app_lulu.vars={}

app_lulu.questions={}
app_lulu.questions['How many eyes do you have?']=('1','2','3')
app_lulu.questions['Which fruit do you like best?']=('banana','mango','pineapple')
app_lulu.questions['Do you like cupcakes?']=('yes','no','maybe')

app_lulu.nquestions=len(app_lulu.questions)
#should be 3

@app_lulu.route('/index_lulu',methods=['GET','POST'])
def index_lulu():
    nquestions=app_lulu.nquestions
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

        return redirect('/main_lulu')

@app_lulu.route('/main_lulu')
def main_lulu2():
    if len(app_lulu.questions)==0 : return render_template('end_lulu.html')
    return redirect('/next_lulu')

#####################################
## IMPORTANT: I have separated /next_lulu INTO GET AND POST
## You can also do this in one function, with If and Else.

@app_lulu.route('/next_lulu',methods=['GET'])
def next_lulu():  #remember the function name does not need to match the URL
    # for clarity (temp variables):
    n=app_lulu.nquestions-len(app_lulu.questions)+1
    q=app_lulu.questions.keys()[0] #python indexes at 0
    # q = list(app.questions.keys())[0] #python indexes at 0
	# Anuar Edition for Pytho 3.4 from following Stackflow source: http://stackoverflow.com/questions/28467967/unhashable-type-dict-keys-works-in-ver-2-7-5-but-not-in-3-4
	# In python3, as opposed to python2, keys returns an iterable set-like view object, not a list. Thus, the need to call the list function on that object to convert it into a list.
    a1=app_lulu.questions[q][0]
    a2=app_lulu.questions[q][1]
    a3=app_lulu.questions[q][2]

    # save current question
    app_lulu.currentq=q

    return render_template('layout_lulu.html',num=n,question=q,ans1=a1,ans2=a2,ans3=a3)

@app_lulu.route('/next_lulu',methods=['POST'])
def next_lulu2():  #can't have two functions with the same name
    # Here, we will collect data from the user.
    # Then, we return to the main function, so it can tell us whether to 
    # display another question page, or to show the end page.

    f=open('%s_%s.txt'%(app_lulu.vars['name'],app_lulu.vars['age']),'a') #a is for append
    f.write('%s\n'%(app_lulu.currentq))
    f.write('%s\n\n'%(request.form['answer_from_layout_lulu'])) #do you know where answer_lulu comes from?
    f.close()

    app_lulu.questions.pop(app_lulu.currentq)

    return redirect('/main_lulu')

if __name__ == "__main__":
    app_lulu.run()
