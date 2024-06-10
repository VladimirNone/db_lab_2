from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sector(db.Model):
    __tablename__ = 'sector'
    id = db.Column(db.Integer, primary_key=True)
    coordinates = db.Column(db.String(255))
    light_intensity = db.Column(db.Float)
    foreign_objects = db.Column(db.Text)
    num_sky_objects = db.Column(db.Integer)
    num_undefined_objects = db.Column(db.Integer)
    num_defined_objects = db.Column(db.Integer)
    notes = db.Column(db.Text)
    date_update = db.Column(db.DateTime)

class Objects(db.Model):
    __tablename__ = 'objects'
    object_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255))
    determination_accuracy = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    time = db.Column(db.Time)
    date = db.Column(db.Date)
    note = db.Column(db.Text)

class NaturalObjects(db.Model):
    __tablename__ = 'natural_objects'
    object_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255))
    galaxy = db.Column(db.String(255))
    accuracy = db.Column(db.Float)
    light_flux = db.Column(db.Float)
    note = db.Column(db.Text)

class Position(db.Model):
    __tablename__ = 'position'
    position_id = db.Column(db.Integer, primary_key=True)
    earth_position = db.Column(db.String(255))
    sun_position = db.Column(db.String(255))
    moon_position = db.Column(db.String(255))

class Relations(db.Model):
    __tablename__ = 'relations'
    relation_id = db.Column(db.Integer, primary_key=True)
    sector_id = db.Column(db.Integer, db.ForeignKey('sector.id'))
    object_id = db.Column(db.Integer, db.ForeignKey('objects.object_id'))
    natural_object_id = db.Column(db.Integer, db.ForeignKey('natural_objects.object_id'))
    position_id = db.Column(db.Integer, db.ForeignKey('position.position_id'))
