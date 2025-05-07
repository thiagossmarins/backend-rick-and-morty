from src.models import db
from src.models.characters_model import Characters

class CharacterRepositories:
  def __init__(self):
    self.session = db.session

  def get_all_characters(self, limit, offset, search_term=None):
    try:
        query = self.session.query(Characters)

        if search_term:
          query = query.filter(Characters.name.ilike(f"%{search_term}%"))

        total = query.count()
        characters = query.limit(limit).offset(offset).all()

        return characters, total

    except Exception:
      print("Error on my repositorie")

  def get_by_id(self, character_id):
    try:
        character = self.session.query(Characters).get(character_id)
        return character
    except Exception as e:
        print(f"Erro no repository: {e}")
        return None