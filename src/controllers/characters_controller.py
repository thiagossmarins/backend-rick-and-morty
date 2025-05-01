from flask import jsonify, request
from src.services.characters_services import CharacterService

class CharactersController:
  def __init__(self):
    self.character_service = CharacterService()

  def getAllCharacters(self):
    try: 
      page = int(request.args.get('page', 1))
      term = request.args.get('term', None)

      result = self.character_service.getAllCharacters(page, term)

      return jsonify(result), 200
    except Exception as e:
      print(f"Erro no controller: {e}")
      return jsonify({
        "erro": "aconteceu algum erro"
      }), 500