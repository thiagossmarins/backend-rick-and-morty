from src.models import db, ma

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Characters {self.name}>"

class CharactersOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    species = ma.String()
    image = ma.String()

characters_output = CharactersOutput(many=True)