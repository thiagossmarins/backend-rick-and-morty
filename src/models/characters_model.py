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
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'),nullable=True)
    
    origin = db.relationship('Locations', foreign_keys=[origin_id], uselist=False, lazy=True, back_populates='character_origin')
    location = db.relationship('Locations', foreign_keys=[location_id], uselist=False, lazy=True, back_populates='character_location')
    episodes = db.relationship('Episodes', secondary='characters_episodes', back_populates='characters')

    @property
    def last_seen(self):
        return self.episodes[-1].air_date

    def __repr__(self):
        return f"<Characters {self.name}>"

class CharactersOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    species = ma.String()
    image = ma.String()
    status = ma.String()

class CharacterOutput(CharactersOutput):
    type = ma.String()
    gender = ma.String()
    origin = ma.Nested('LocationsOutput')
    location = ma.Nested('LocationsOutput')
    last_seen = ma.String(attribute="last_seen")

characters_output = CharactersOutput(many=True)
character_output = CharacterOutput()