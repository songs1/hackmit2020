from my_app import app, db, check_status
from flask import render_template, request, redirect
from my_app.models import User
import json
import time

@app.route("/")
def index():
    db_users = User.query.all()
    users_list = [{"first":u.first, "last":u.last, "dob":u.dob, "county":u.county, "email":u.email} for u in db_users]

    
    #return render_template("index.html")
    return render_template("index.html", views_out = reversed(users_list))
    

@app.route("/add_user", methods=['POST'])
def add_user():
    if request.method == "POST":
        info = request.get_json()
        statusGood = False
        if info['first']!= "" and info['last']!= "" and info['dob']!="" and info['county']!="":
            statusGood = check_status.check_status(first_initial=info['first'], last_name=info['last'], DOB=info['dob'], county=info['county'])
        
        if statusGood:
            new_user = User(first=info['first'], last=info['last'], dob=info['dob'], county=info['county'], email=info['email'])
            db.session.add(new_user)
            db.session.commit()
            return "yes"
        else:
            return "no"

@app.route("/form-submit")
def form_submit():
    
    db_users = User.query.all()
    users_list = [{"first":u.first, "last":u.last, "dob":u.dob, "county":u.county, "email":u.email} for u in db_users]

    return render_template("form-submit.html", views_out=users_list)

    

#@app.route('/', methods=['POST'])
#def form():
#    return render_template('form.html')

"""@app.route('/submitted', methods=['POST'])
def submitted():
    return render_template('submitted.html', say=request.form['say'], to=request.form['to'])"""

