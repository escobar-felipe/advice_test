from unicodedata import name
from carford.models import User, Owner,  Vehicles, Vehicle_owner


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the name and password fields are defined correctly
    """
    user = User(username='test_admin' ,password = '1234')
    assert user.username == 'test_admin'
    assert user.password == '1234'

def test_new_owner():
    """
    GIVEN a User model
    WHEN a new Onwer is created
    THEN check the name fields is defined correctly
    """
    owner = Owner(name='test_owner')
    assert owner.name == 'test_owner'
    
def test_new_vehicle():
    """
    GIVEN a User model
    WHEN a new Vehicle is created
    THEN check the model, brand, and color fields are defined correctly
    """
    vehicle = Vehicles(color='blue' ,brand = 'bmw', model='sedan')
    assert vehicle.color == 'blue'
    assert vehicle.brand == 'bmw'
    assert vehicle.model == 'sedan'

def test_new_owner_vehicle():
    """
    GIVEN a User model
    WHEN a new Vehicle_owner is created
    THEN check the id_owner and id_vehicle are defined correctly
    """
    vehicle_owner = Vehicle_owner(id_owner=1,id_vehicle =1)
    assert vehicle_owner.id_owner == 1
    assert vehicle_owner.id_vehicle == 1
