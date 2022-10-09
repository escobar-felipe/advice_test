from carford.ext.database import db
from sqlalchemy_serializer import SerializerMixin

class Vehicle_owner(db.Model, SerializerMixin):
    id= db.Column(db.Integer, primary_key=True)
    id_owner = db.Column(db.Integer)
    id_vehicle= db.Column(db.Integer)

class Vehicles(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(140))
    color = db.Column(db.String(140))
    model = db.Column(db.String(140))

class Owner(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), unique=True, nullable=False)

class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140), unique=True, nullable=False)
    password = db.Column(db.String(512))