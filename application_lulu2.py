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

        return render_template('layout_lulu.html',num=1,question='How many eyes do you have?',ans1='1',ans2='2',ans3='3')

@app_lulu.route('/next_lulu',methods=['POST'])
def next_lulu():
    return redirect('/usefulfunction_lulu')

@app_lulu.route('/usefulfunction_lulu',methods=['GET','POST'])
def usefulfunction_lulu():
    return render_template('layout_lulu.html',num=1,question='Which fruit do you like best?',ans1='banana',ans2='mango',ans3='pineapple')

if __name__ == "__main__":
    app_lulu.run()
