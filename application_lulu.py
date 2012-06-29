from flask import Flask,render_template
app_lulu = Flask(__name__)

@app_lulu.route('/index_lulu')
def index_lulu():
    nquestions=5
    return render_template('userinfo_lulu.html',num=nquestions)

if __name__ == "__main__":
    app_lulu.run()
