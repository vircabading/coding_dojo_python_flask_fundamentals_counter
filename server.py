import datetime
from flask import Flask, render_template, session
from werkzeug.datastructures import RequestCacheControl
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = "TiYSKDNRitA!"                                                     # This is Your Secret Key Do Not Reveal it to Anyone!

@app.route('/')                                                                     # Main Page
def index():
    if 'num_visits' in session:                                                     # If  num_visits key exists
        session['num_visits'] += 1                                                  #   increment num_visits by 1
        print("Session key num_visits:", session['num_visits'] )
    else:                                                                           # If num_visits key doesn't exist
    session['num_visits'] = 1                                                       #   initialize num_visits to 1
        print("Session key num_visits:", session['num_visits'] )
    return render_template("index.html")

@app.route('/clear')
def clear():                                                                        # Clears the num_visits
session.clear();                                                                    #   then redirect to index
    return redirect("/")

@app.route('/add2')                                                                 # adds 2 to num_visits by
def add2():                                                                         #   by incrementing num_visits then returning to index
    if 'num_visits' in session:
        session['num_visits'] += 1
        print("Session key num_visits:", session['num_visits'] )
    else:
        session['num_visits'] = 1
        print("Session key num_visits:", session['num_visits'] )
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    