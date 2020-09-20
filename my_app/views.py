from my_app import app, db
from flask import render_template, request, redirect
from my_app.models import User


@app.route("/")
def index():
    """db_users = User.query.all()
    users_list = [{"First Initial":u.first, "Last Name":u.last, "Date of Birth":u.dob, "County":u.county, "Email":u.email} for u in db_users]"""


    return render_template("index.html",)
    

@app.route("/add_user", methods=['POST'])
def add_user():
    if request.method == "POST":
        info = request.get_json()
        print(info)
        #new_user = User(first=info['first'], last=info['last'], dob=info['dob'], county=info['county'], email=info['email'])
        #db.session.add(new_user)
        #db.session.commit()
    return render_template("add_user.html", info = info)
    
#@app.route("/post",

#@app.route('/', methods=['POST'])
#def form():
#    return render_template('form.html')

"""@app.route('/submitted', methods=['POST'])
def submitted():
    return render_template('submitted.html', say=request.form['say'], to=request.form['to'])"""

