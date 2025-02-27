# Imports
from flask import Flask, render_template, redirect, request
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

@app.route("/login")
def login():
    return render_template("login.html")




if __name__ in "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)