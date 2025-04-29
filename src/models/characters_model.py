from src.models import db

class Characters(db.Model):
  __tablename__ = 'characters'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(100), nullable=False )
  status = db.Column(db.String(50), nullable=False )
  species = db.Column(db.String(50), nullable=False )
  type = db.Column(db.String(50), nullable=False )
  gender = db.Column(db.String(10), nullable=False )
  image = db.Column(db.String(255), nullable=False )
  origin_id = db.Column(db.Integer, nullable=False )
  location_id = db.Column(db.Integer, nullable=False )

  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "status": self.status,
      "species": self.species,
      "type": self.type,
      "gender": self.gender,
      "image": self.image,
      "origin_id": self.origin_id,
      "location_id": self.location_id
  }

  def __repr__(self):
      return f"<Characters {self.name}>"
  
print(Characters)