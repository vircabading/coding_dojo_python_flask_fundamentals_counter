import datetime
from flask import Flask, render_template, session
from werkzeug.datastructures import RequestCacheControl

app = Flask(__name__)
app.secret_key = "TiYSKDNRitA!"                                                     # This is Your Secret Key Do Not Reveal it to Anyone!

@app.route('/')                                                                     # Main Page
def index():
    if 'num_visits' in session:
        print("Session key num_visits:", session['num_visits'] )
    else:
        session['num_visits'] = 1
    return render_template("index.html")

if __name__=="__main__":   
    app.run(debug=True)    