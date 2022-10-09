from flask_wtf import FlaskForm
from wtforms import SubmitField,SelectField, StringField

class Add_Vehicle(FlaskForm):
    color = SelectField("Color", choices=[("yellow","yellow"),("blue","blue"),("grey","grey")])
    model = SelectField("Model",choices=[("hatch","hatch"),("sedan","sedan"),("convertible","convertible")])
    brand = SelectField("Brand", choices=[("audi","audi"),("bmw","bmw"),("jeep","jeep"),("porshe","porshe")])
    owner = SelectField("Owner",choices=[])
    add_vehicle = SubmitField("Add Vehicle")

class Add_Owner(FlaskForm):
    name= StringField("Name")