from src.utils.response_handle import api_response
from flask import jsonify, request
from src.services.characters_services import CharacterService
from werkzeug.exceptions import NotFound

class CharactersController:
    def __init__(self):
        self.character_service = CharacterService()

    def get_all_characters(self):
        try:
            page = request.args.get("page", default=1, type=int)
            name = request.args.get("name", default=None, type=str)

            result = self.character_service.get_all_characters(page, name)
            return api_response(
                True,
                "Characters encontrados com sucesso",
                {"characters": result},
                200
            )

        except Exception as e:
            print(f"Erro no controller: {e}")
            return api_response(
                False,
                f"Ocorreu um erro ao buscar os characters: {str(e)}",
                None,
                500
            )

    def get_by_id(self, character_id):
        try:
            result = self.character_service.get_by_id(character_id)

            return api_response(
                True,
                "Character encontado com sucesso",
                {"character": result},
                200
            )
        except NotFound as e:
            return api_response(
                False,
                f"Personagem não encontrado: {str(e)}",
                None,
                404
            )
        except Exception as e:
            return api_response(
                False,
                f"Ocorreu um erro ao buscar os characters: {str(e)}",
                None,
                500
            )