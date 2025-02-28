from extension import db

# A database model
class MyThing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thing = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Double(7, 2))
    link = db.Column(db.String(100))

    def __repr__(self) -> str:
        return f"Task {self.id}"
    
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    shirt = db.Column(db.String(100))
    pants = db.Column(db.Integer)
    shoes = db.Column(db.Integer)

    def __init__(self, name, password):
        self.name = name
        self.password = password

class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    name = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(30), nullable=False)
    #date = db.Column(db.Date, nullable=False)

    def __init__(self, name, date):
        self.name = name
        self.dare = date

class Shared(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id), primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey(Event.event_id), primary_key=True)

class List(db.Model):
    list_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    event_id = db.Column(db.Integer, db.ForeignKey(Event.event_id))

class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey(List.list_id))
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer)
    link = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name