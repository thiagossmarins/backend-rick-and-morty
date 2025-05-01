from src.models import db
from src.models.characters_model import Characters

class CharacterRepositories:
  def __init__(self):
    self.session = db.session

  def getAllCharacters(self, limit, offset, search_term=None):
    try:
        query = self.session.query(Characters)

        if search_term:
          query = query.filter(Characters.name.ilike(f"%{search_term}%"))

          total = query.count()

          characters = query.limit(limit).offset(offset).all()

          return characters, total

    except Exception:
      print("Error on my repositorie")