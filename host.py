from flask import Flask, render_template, redirect, request
from flask.globals import session
app = Flask(__name__)
app.secret_key = '123456'



@app.route('/')
def start():
    if 'staycount' in session:
        # refreshcounter=session['staycount']
        # refreshcounter += 1
        # session['staycount']= refreshcounter
        session['staycount'] += 1
    else:
        # refreshcounter = 1
        # session['staycount']= refreshcounter
        session['staycount'] = 1
    
    return render_template('index.html')







if __name__ == "__main__":
    app.run(debug=True)