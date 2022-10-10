from flask import abort, render_template
from carford.models import Vehicles,  Owner, Vehicle_owner
from carford.ext.database import db
from carford.ext.forms import Add_Owner, Add_Vehicle, Owners

def index():
    try:
        opportunities = Owner.query.join(Vehicle_owner, Vehicle_owner.id_owner==Owner.id , isouter=True).filter(Vehicle_owner.id_owner == None).all()
        owners = Owner.query.join(Vehicle_owner,Vehicle_owner.id_owner==Owner.id).filter(Vehicle_owner.id_owner != None).distinct()
    except:
        opportunities = []
        owners = []        
    form_vehicle = Add_Vehicle()
    form_owner = Add_Owner()
    form_vehicle.owner.choices= [(owner.id,owner.name) for owner in opportunities]
    return render_template("index.html", opportunities=opportunities, owners=owners, form_owner=form_owner, form_vehicle=form_vehicle)


def owner_page(owner_id):
    vehicles_owners = db.session.query(Owner, Vehicle_owner, Vehicles).join(Vehicle_owner,Vehicle_owner.id_vehicle==Vehicles.id).join(Owner, Vehicle_owner.id_owner==Owner.id).filter(Vehicle_owner.id_owner == owner_id).all() or abort(
        404, "vehicles not finded"
    )
    form_owners= Owners()
    owners = Owner.query.filter(Owner.id != owner_id).all()
    form_owners.owner.choices= [(owner.id,owner.name) for owner in owners]
    form_vehicle = Add_Vehicle()
    owner_page = Owner.query.filter(Owner.id == owner_id).first()
    form_vehicle.owner.choices= [(owner_page.id,owner_page.name)]
    return render_template("owner.html", vehicles_owners=vehicles_owners, form_owners=form_owners, form_vehicle=form_vehicle)
