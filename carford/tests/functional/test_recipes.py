import json
from flask import jsonify
def test_home_page(client):
    """
    GIVEN a Flask application 
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """

    # Create a test client using the Flask application 
    response = client.get('/')
    assert response.status_code == 200


def test_vehicle_information(client, db_information):
    """
    GIVEN a Flask application 
    WHEN the vehicle_information is requested (GET)
    THEN check that the response is valid
    """
    owners , vehicles , vehicles_owners = db_information

    response= client.get(f'/api/v1/vehicles/{vehicles[2].id}')
    assert response.status_code == 200


def test_delete_owner(client, db_information):
    """
    GIVEN a Flask application 
    WHEN the owner is delete by requested (delete)
    THEN check that the response is valid
    """
    owners , vehicles , vehicles_owners = db_information
    response= client.delete(f'/api/v1/deleteowner/{owners[0].id}')
    assert response.status_code == 200
