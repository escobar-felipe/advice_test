from flask import abort, jsonify, make_response
from flask_restful import Resource
from flask import request
from carford.ext.database import db
from carford.models import Vehicles , Vehicle_owner , Owner

def abort_if_vehicle_doesnt_exist(vehicle_id):
    vehicle = Vehicles.query.where(Vehicles.id ==vehicle_id).first()
    if not vehicle:
        abort(404, "Vehicle_id = {} doesn't exist".format(vehicle_id))
    else:
        return make_response("sucess", 200)

def abort_if_owner_doesnt_exist(owner_id):
    owner = Owner.query.where(Owner.id ==owner_id).first()
    if not owner:
        abort(404, "Owner_id = {} doesn't exist".format(owner_id))
    else:
        return make_response("sucess", 200)

def check_number_of_vehicle(owner_id):
    vehicles_owner = Vehicle_owner.query.where(Vehicle_owner.id_owner==owner_id).count()
    if vehicles_owner < 3:
        return vehicles_owner
    else:
        abort(500, "Owner_id = {} has 3 cars".format(owner_id))

class VehiclesResource(Resource):
    def get(self, vehicle_id):
        abort_if_vehicle_doesnt_exist(vehicle_id)
        vehicle = Vehicles.query.where(Vehicles.id ==vehicle_id).first()
        return jsonify(vehicle.to_dict())

    def put(self, vehicle_id):
        abort_if_vehicle_doesnt_exist(vehicle_id)
        req = request.json
        check_number_of_vehicle(req['owner'])
        update_owner =  Vehicle_owner.query.filter(Vehicle_owner.id_vehicle == vehicle_id).first()
        number_vehicle = Vehicle_owner.query.where(Vehicle_owner.id_owner==update_owner.id_owner).count()
        update_owner.id_owner= req['owner'] #id_new_owner
        db.session.commit()

        return make_response(jsonify(
            {"Vehicle_{}".format(vehicle_id): "updated",
             "number_vehicle":number_vehicle
            }
        ),200)

    def delete(self,vehicle_id):
        abort_if_vehicle_doesnt_exist(vehicle_id)
        Vehicles.query.filter(Vehicles.id == vehicle_id).delete()
        vehicle_owner = Vehicle_owner.query.filter(Vehicle_owner.id_vehicle == vehicle_id)
        number_vehicle = Vehicle_owner.query.where(Vehicle_owner.id_owner==vehicle_owner.first().id_owner).count()
        vehicle_owner.delete()
        db.session.commit()
        
        return jsonify(
            {"Vehicle_{}".format(vehicle_id): "deleted",
             "number_vehicle":number_vehicle
            }
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
        
        return make_response(jsonify(
            {"Vehicle": "added",
             "owner_id":req['owner']
            }
        ),200)

class OwnerResource(Resource):
    def post(self):
        req = request.form
        add_owner = Owner(name=req['name'])
        db.session.add(add_owner)
        db.session.commit()

        return make_response(jsonify(
            {"Add_Owner": "sucess"}
        ),200)

class DeleteOwnerResource(Resource):
    def delete(self, id_owner):
        abort_if_owner_doesnt_exist(id_owner)

        for vehicle in Vehicle_owner.query.filter(Vehicle_owner.id_owner == id_owner).all():
            Vehicles.query.filter(Vehicles.id == vehicle.id_vehicle).delete()

        Vehicle_owner.query.filter(Vehicle_owner.id_owner == id_owner).delete()
        Owner.query.filter(Owner.id == id_owner).delete()
        db.session.commit()

        return jsonify(
            {"Delete Owner": "sucess"}
        )
