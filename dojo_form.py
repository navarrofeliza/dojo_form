from flask import Flask, render_template, session, redirect,request

app = Flask(__name__)

app.secret_key="Hello there."

@app.route('/')
def index():
    return render_template("form.html")

@app.route('/process',methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['email']
    session['language'] = request.form['role']
    session['comments'] = request.form['comments']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('results.html')
    
if __name__=="__main__":
    app.run(debug=True)