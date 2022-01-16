from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = "General Kenobi...."

@app.route('/')
def index():
    session["loggedOn"] = False
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create():

    first = request.form['firstName']
    last = request.form['lastName']
    email = request.form['email']
    password = request.form['password']
    hashed_password = md5.new(password).hexdigest()
    confirm = request.form['confirm']
    
    
    properLogin = True
    if len(first) < 3:
        flash("First name must be filled!")
        properLogin = False

    if len(last) < 3:
        flash("Last name must be filled!")
        properLogin = False

    my_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') # I hope this is right
    check = "SELECT * FROM users"
    if not my_re.match(email):
        flash("Use a verified email!")
        properLogin = False
    
    if len(password) < 8:
        flash("Password must be 8 characters long!")
        properLogin = False
    if password != confirm:
        flash("Passwords must match!")
        properLogin = False
    
    if properLogin:
        flash("Hello there!".format(first, last))
        return redirect('/')
    else:
        return redirect('/')

app.run(debug=True)