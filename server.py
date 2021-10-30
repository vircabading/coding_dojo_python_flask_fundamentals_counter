import datetime
from flask import Flask, render_template, session, redirect, request

from werkzeug.datastructures import RequestCacheControl
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = "TiYSKDNRitA!"                                                     # This is Your Secret Key Do Not Reveal it to Anyone!

@app.route('/')                                                                     # Main Page
def index():
    if 'num_visits' and 'count' in session:                                                     # If  num_visits key exists
        session['num_visits'] += 1                                                  #   increment num_visits by 1
        session['count'] += 1
        print("Session key num_visits:", session['num_visits'] )
    else:                                                                           # If num_visits key doesn't exist
        session['num_visits'] = 1                                                       #   initialize num_visits to 1
        session['count'] = 1
        print("Session key num_visits:", session['num_visits'] )
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():                                                              # Clears the num_visits
    session.clear();                                                                    #   then redirect to index
    return redirect("/")

@app.route('/add2')                                                                 # adds 2 to counter by
def add2():                                                                         #   by incrementing counter by 1 then returning to index
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return redirect('/')

@app.route('/increment_by', methods=['POST'])
def increment_by():
    session['increment_by'] = int(request.form['increment_by'])-1                 # remember to decrease increment_by by one because will increment by 1 when redirected to "/"
    session['count'] += session['increment_by']
    print("in increment_by:", session['increment_by'])
    return redirect("/")

if __name__=="__main__":   
    app.run(debug=True)    