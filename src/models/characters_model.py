from src.models import db

class Characters(db.Model):
  __tablename__ = 'characters'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(100), nullable=False )
  species = db.Column(db.String(50), nullable=False )
  image = db.Column(db.String(255), nullable=False )

  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "species": self.species,
      "image": self.image,
  }

  def __repr__(self):
      return f"<Characters {self.name}>"
  
print(Characters)