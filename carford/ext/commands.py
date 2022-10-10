import click
from carford.ext.database import db
from carford.ext.auth import create_user
from carford.models import Vehicles , Owner, Vehicle_owner


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        Vehicles(id=1, brand = "Audi", color="blue", model="hatch"),
        Vehicles(id=2, brand = "Jeep", color="yellow", model="hatch"),
        Vehicles(id=3, brand = "Bmw", color="blue", model="sedan"),
        Vehicles(id=4, brand = "Porshe", color="gray", model="convertible"),
        Owner(id=1,name='Felipe'),
        Owner(id=2,name='Gabriela'),
        Owner(id=3,name='Audrey'),
        Owner(id=4,name='Guilherme'),
        Vehicle_owner(id=1, id_owner=1, id_vehicle=1),
        Vehicle_owner(id=2, id_owner=1, id_vehicle=2),
        Vehicle_owner(id=3, id_owner=2, id_vehicle=3),
        Vehicle_owner(id=4, id_owner=1, id_vehicle=4),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    # return 3 querys for tests
    return Owner.query.all() , Vehicles.query.all() ,Vehicle_owner.query.all(),
    


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(username, password):
        """Adds a new user to the database"""
        return create_user(username, password)
