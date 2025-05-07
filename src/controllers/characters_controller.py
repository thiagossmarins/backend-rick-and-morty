from flask import jsonify, request
from src.services.characters_services import CharacterService

class CharactersController:
    def __init__(self):
        self.character_service = CharacterService()

    def get_all_characters(self):
        try:
            page = request.args.get("page", default=1, type=int)
            name = request.args.get("name", default=None, type=str)

            result = self.character_service.get_all_characters(page, name)
            return jsonify(result), 200

        except Exception as e:
            print(f"Erro no controller: {e}")
            return jsonify({
                "erro": "aconteceu algum erro"
            }), 500

    def get_by_id(self, character_id):
        try:
            result = self.character_service.get_by_id(character_id)

            if result:
                return jsonify(result), 200
            else:
                return jsonify({"error": "Personagem não encontrado"}), 404
        except Exception as e:
            print(f"Erro no controller: {e}")
            return jsonify({"erro": "aconteceu algum erro"}), 500
