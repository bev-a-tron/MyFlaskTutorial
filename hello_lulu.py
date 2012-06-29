from flask import Flask
app_lulu = Flask(__name__)

@app_lulu.route('/hello_lulu2')
def hello_lulu():
    return 'Hello World'

if __name__ == '__main__':
    app_lulu.run()

