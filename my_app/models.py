#first, last, dob, county, phone, email, status

from my_app import db

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(1))
    last = db.Column(db.String(50))
    county = db.Column(db.String(50))
    dob = db.Column(db.Integer)
    email = db.Column(db.String(50))
    status = db.Column(db.String(20))