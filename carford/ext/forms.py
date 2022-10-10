from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import InputRequired


class Add_Vehicle(FlaskForm):
    color = SelectField("Color", choices=[("yellow","yellow"),("blue","blue"),("grey","grey")],validators=[InputRequired()])
    model = SelectField("Model",choices=[("hatch","hatch"),("sedan","sedan"),("convertible","convertible")],validators=[InputRequired()])
    brand = SelectField("Brand", choices=[("audi","audi"),("bmw","bmw"),("jeep","jeep"),("porshe","porshe")],validators=[InputRequired()])
    owner = SelectField("Owner",choices=[] ,validators=[InputRequired()])

class Add_Owner(FlaskForm):
    name= StringField("Name",validators=[InputRequired()])

class Owners(FlaskForm):
    owner = SelectField("Owner",choices=[], validators=[InputRequired()])
