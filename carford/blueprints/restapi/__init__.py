from flask import Blueprint
from flask_restful import Api

from .resources import VehiclesResource, AddCarOwnerResource, AddOwner

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(VehiclesResource, "/vehicles/<int:vehicle_id>", endpoint= "vehicleresource")
    api.add_resource(AddCarOwnerResource, "/addvehicles/", endpoint= "addvehicle")
    api.add_resource(AddOwner, "/addowner/", endpoint= "addowner")
    app.register_blueprint(bp)