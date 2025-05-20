from src.models.characters_model import characters_output, character_output
from src.repositories.characters_repository import CharacterRepositories
from werkzeug.exceptions import NotFound
import math

class CharacterService():
    def __init__(self):
        self.character_repository = CharacterRepositories()

    def get_all_characters(self, page, name=None):
        limitCharactersPage = 20
        offset = (page - 1) * limitCharactersPage

        characters, total = self.character_repository.get_all_characters(
            limitCharactersPage,
            offset,
            name
        )

        totalPages = math.ceil(total / limitCharactersPage)
        data = characters_output.dump(characters)
        return {
            "characters": data,
            "totalPages": totalPages,
            "currentPage": page
        }

    def get_by_id(self, character_id):
        character = self.character_repository.get_by_id(character_id)
        data = character_output.dump(character)
        if character:
            return data
        else:
            raise NotFound(f"Personagem com ID {character_id} não encontrado")