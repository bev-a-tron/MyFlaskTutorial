Connecting an application with HTML
===================================

Copy ``hello_lulu.py``.  Call the new file ``application.py``.  We will edit this file 
to produce a web application that will display the HTML form when the specified URL is
accessed.

Inside ``application.py``, edit the file to look like this::

       from flask import Flask,render_template
       app_lulu = Flask(__name__)
       
       @app_lulu.route('/index_lulu')
       def index_lulu():
           return render_template('userinfo_lulu.html')

       if __name__ == "__main__":
           app_lulu.run()

You can try running it now with::

    python application.py

Open a browser window and go to::
    
    127.0.0.1:5000/index

You should see the form we just made.  