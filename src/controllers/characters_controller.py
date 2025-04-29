from flask import jsonify
from src.models.characters_model import Characters

class CharactersController:
  def getAllCharacters(self):
    try: 
      characters = Characters.query.all()
      return jsonify([char.to_dict() for char in characters]), 200
    except Exception:
      return jsonify({
        "erro": "aconteceu algum erro"
      }), 500