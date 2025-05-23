from src.models import db, ma
from sqlalchemy import func
from marshmallow import fields

class Locations(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=True)
    dimension = db.Column(db.String(100), nullable=False)

    character_origin = db.relationship('Characters', foreign_keys='Characters.origin_id', uselist=True, lazy=True, back_populates='origin')
    character_location = db.relationship('Characters', foreign_keys='Characters.location_id', uselist=True, lazy=True, back_populates='location')

    @property
    def residents_count(self):
        return len(self.character_location)

    def __repr__(self):
        return f"<Locations {self.name}>"

class LocationsOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    type = ma.String()
    dimension = ma.String()
    residents_count = ma.String(attibute="residents_count")