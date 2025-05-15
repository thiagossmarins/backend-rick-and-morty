from src.models import db, ma

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)

    origin_id = db.Column(db.Integer, db.ForeignKey('locations.id'),nullable=True)
    origin = db.relationship('Locations', foreign_keys=[origin_id], uselist=False, lazy=True, back_populates='character_origin')
    
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'),nullable=True)
    location = db.relationship('Locations', foreign_keys=[location_id], uselist=False, lazy=True, back_populates='character_location')


    def __repr__(self):
        return f"<Characters {self.name}>"

class CharactersOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    species = ma.String()
    image = ma.String()

class CharacterOutput(CharactersOutput):
    status = ma.String()
    type = ma.String()
    gender = ma.String()
    origin = ma.Nested('LocationsOutput')
    location = ma.Nested('LocationsOutput')

characters_output = CharactersOutput(many=True)
character_output = CharacterOutput()