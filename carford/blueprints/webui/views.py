from flask import abort, render_template
from carford.models import Vehicles,  Owner, Vehicle_owner
from carford.ext.database import db
from carford.ext.forms import Add_Owner, Add_Vehicle


def index():
    opportunities = Owner.query.join(Vehicle_owner, Vehicle_owner.id_owner==Owner.id , isouter=True).filter(Vehicle_owner.id_owner == None).all()
    owners = Owner.query.join(Vehicle_owner,Vehicle_owner.id_owner==Owner.id).filter(Vehicle_owner.id_owner != None).distinct()
    form_vehicle = Add_Vehicle()
    form_owner = Add_Owner()
    form_vehicle.owner.choices= [(owner.id,owner.name) for owner in opportunities]
    return render_template("index.html", opportunities=opportunities, owners=owners, form_owner=form_owner, form_vehicle=form_vehicle)


def vehicles(owner_id):
    vehicles = db.session.query(Owner, Vehicle_owner, Vehicles).join(Vehicle_owner,Vehicle_owner.id_vehicle==Vehicles.id).join(Owner, Vehicle_owner.id_owner==Owner.id).filter(Vehicle_owner.id_owner == owner_id).all() or abort(
        404, "vehicles not finded"
    )
    return render_template("owner.html", vehicles=vehicles)
