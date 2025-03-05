# Imports
from flask import Flask, render_template, redirect, request, jsonify, session
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from extension import db, app
import fillDB
from models import *


# Homepage
@app.route("/", methods=["POST", "GET"])
def index():
    # Add data
    if request.method == "POST":
        current_thing = request.form['content']
        new_thing = MyThing(thing=current_thing)
        try:
            db.session.add(new_thing)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"ERROR:{e}")
            return f"ERROR:{e}"
    
    # View data
    else:
        things = MyThing.query.order_by(MyThing.thing).all()
        return render_template("index.html", things=things)
    

# Delete a thing
@app.route("/delete/<int:id>")
def delete(id:int):
    delete_thing = MyThing.query.get_or_404(id)
    try:
        db.session.delete(delete_thing)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"ERROR:{e}"
    
# Update a thing
@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id:int):
    thing = MyThing.query.get_or_404(id)
    if request.method == "POST":
        thing.thing = request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"ERROR:{e}"
    else:
        return render_template('update.html',thing=thing)
'''
All routes above are examples for reference. They will be deleted later as the project
gets closer to being complete
'''

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        try:
            fillDB.popDB(db)
            return render_template("admin.html", flag="False")
        except Exception as e:
            return f"ERROR:{e}"
    if request.method == "GET":
        user = User.query.filter_by(name="test").first()
        if user:
            return render_template("admin.html", flag=user)
    return render_template("admin.html", flag="True")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method  == "POST":
        data = request.form
        userVerify = User.query.filter_by(name=data['user'], password=data['password']).one_or_none()
        if userVerify:
            session['user'] = data['user']
            return redirect("/home")
        else:
            return "No"

    if request.method == "GET":   
        session.pop('user', None)
        try:
            users = User.query.all()
            return render_template("login.html", users=users)
        except Exception as e:
            return f"ERROR:{e}"
        

'''
I don't understand what I was doing wrong before, but this works now. I am not going to use
this method, howver. I was planning on making this its own function, but I think it's fine
to keep in the main login function.
'''
# @app.route("/loginCheck", methods=["POST"])
# def loginCheck():
#     if request.method  == "POST":
#         data = request.form
#         userVerify = User.query.filter_by(name=data['user'], password=data['password']).one_or_none()
#         if userVerify:
#             return redirect("/home")
#         else:
#             return "No"

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method  == "POST":
        data = request.form
        userVerify = User.query.filter_by(name=data['user']).one_or_none()
        if userVerify:
            return "No"
        else:
            newUser = User(name=data['user'], password=data['password'])
            db.session.add(newUser)
            db.session.commit()
            session['user'] = data['user']
            return redirect("/home")

    session.pop('user', None)
    return render_template("signup.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        session.pop('user', None)
        return redirect("/login")
    
    if request.method == "GET":
        if session.get('user'):
            return render_template("home.html", user=session['user'])
        else:
            return redirect("/login")

    return render_template("home.html")



if __name__ in "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)