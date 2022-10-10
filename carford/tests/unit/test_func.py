from carford.blueprints.restapi.resources import abort_if_owner_doesnt_exist, abort_if_vehicle_doesnt_exist

def test_if_owner_doesnt_exist(db_information):
    """
    GIVEN a Function to check owner
    WHEN a owner exist 
    THEN check the status code == 200
    """
    owners , vehicles , vehicles_owners = db_information

    assert abort_if_owner_doesnt_exist(owners[2].id).status_code == 200



def test_if_vehicle_doesnt_exist(db_information):
    """
    GIVEN a Function to check vehicle
    WHEN a vehicles exist 
    THEN check the status code == 200
    """
    owners , vehicles , vehicles_owners = db_information

    assert abort_if_vehicle_doesnt_exist(vehicles[2].id).status_code == 200