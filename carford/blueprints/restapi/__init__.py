from flask import Blueprint
from flask_restful import Api

from .resources import VehiclesResource, AddCarOwnerResource, OwnerResource, DeleteOwnerResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(VehiclesResource, "/vehicles/<int:vehicle_id>", endpoint= "vehicleresource")
    api.add_resource(AddCarOwnerResource, "/addvehicles/", endpoint= "addvehicle")
    api.add_resource(OwnerResource, "/addowner/", endpoint= "addowner")
    api.add_resource(DeleteOwnerResource, "/deleteowner/<int:id_owner>", endpoint="deleteowner")
    app.register_blueprint(bp)