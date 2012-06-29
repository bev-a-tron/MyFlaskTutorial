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
