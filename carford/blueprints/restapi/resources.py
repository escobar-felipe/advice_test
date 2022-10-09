from flask import abort, jsonify , redirect, url_for, flash
from flask_restful import Resource
from flask import request
from carford.ext.database import db
from carford.models import Vehicles , Vehicle_owner , Owner

def abort_if_vehicle_doesnt_exist(vehicle_id):
    vehicle = Vehicles.query.where(Vehicles.id ==vehicle_id).first()
    if not vehicle:
        abort(404, "Vehicle_id = {} doesn't exist".format(vehicle_id))

def abort_if_owner_doesnt_exist(owner_id):
    owner = Owner.query.where(Owner.id ==owner_id).first()
    if not owner:
        abort(404, "Owner_id = {} doesn't exist".format(owner_id))

def check_number_of_vehicle(owner_id):
    vehicles_owner =Vehicle_owner.query.where(Vehicle_owner.id_owner==owner_id).count()
    if vehicles_owner > 3:
        abort(404, "Owner_id = {} has more then 3 cars".format(owner_id))

class VehiclesResource(Resource):
    def get(self, vehicle_id):
        abort_if_vehicle_doesnt_exist(vehicle_id)
        vehicle = Vehicles.query.where(Vehicles.id ==vehicle_id).first()
        return jsonify(vehicle.to_dict())

    def put(self, vehicle_id):
        abort_if_vehicle_doesnt_exist(vehicle_id)
        req = request.form
        update_vehicle = Vehicles.query.where(Vehicles.id == vehicle_id).first()
        update_vehicle.brand = req['brand']
        update_vehicle.color = req['color']
        update_vehicle.model = req['model'] 
        db.session.commit()

        return jsonify(
            {"Vehicle_{}".format(vehicle_id): "updated"}
        )
    
    def delete(self,vehicle_id):
        abort_if_vehicle_doesnt_exist(vehicle_id)
        del_vehicles = Vehicles.query.where(Vehicles.id == vehicle_id)
        del_vehicle_owner = Vehicle_owner.query.where(Vehicle_owner.id_vehicle == vehicle_id)
        db.session.delete([del_vehicles,del_vehicle_owner])
        db.session.commit()

        #return redirect(url_for("webui.ownerview"), owner_id=)
        return jsonify(
            {"Vehicle_{}".format(vehicle_id): "deleted"}
        )

class AddCarOwnerResource(Resource):
    def post(self):
        req = request.form
        abort_if_owner_doesnt_exist(req['owner'])
        check_number_of_vehicle(req['owner'])
        add_vehicle = Vehicles(brand=req['brand'], color=req['color'], model=req['model'])
        db.session.add(add_vehicle)
        db.session.commit()
        db.session.refresh(add_vehicle)

        add_onwer_vehicle = Vehicle_owner(id_vehicle=add_vehicle.id , id_owner=req['owner'])
        db.session.add(add_onwer_vehicle)
        db.session.commit()
        
        return jsonify(
            {"Add vehicle to Owner": "sucess"}
        )
    
class AddOwner(Resource):
    def post(self):
        req = request.form
        add_owner = Owner(name=req['name'])
        db.session.add(add_owner)
        db.session.commit()

        return jsonify(
            {"Add Owner": "sucess"}
        )