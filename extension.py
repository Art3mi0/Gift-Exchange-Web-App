from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
Scss(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# For deployment. Makes it so users get their own database.
# app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)