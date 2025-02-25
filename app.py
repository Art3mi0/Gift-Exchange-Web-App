# Imports
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

# My App
app = Flask(__name__)
Scss(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# For deployment. Makes it so users get their own database.
# app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)


# A database model
class MyThing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thing = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Double(7, 2))
    link = db.Column(db.String(100))

    def __repr__(self) -> str:
        return f"Task {self.id}"


# For deployment. When deployed, will make a fresh db at the start 
# with app.app_context():
#     db.create_all()


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
    
# Casino Page
@app.route("/casino/", methods=["GET"])
def casino():
    # Add data
    if request.method == "GET":
        return render_template('casino.html')


if __name__ in "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# For deployment. Different main and db creation moved elsewhere.
# if __name__ in "__main__":
#     app.run(debug=True)