from src.models.characters_model import Characters
from src.repositories.characters_repositories import CharacterRepositories
import math


class CharacterService():
    def __init__(self):
        self.character_repository = CharacterRepositories()

    def get_all_characters(self, page, term=None):
        limitCharactersPage = 20
        offset = (page - 1) * limitCharactersPage

        characters, total = self.character_repository.get_all_characters(
            limitCharactersPage,
            offset,
            term
        )

        totalPages = math.ceil(total / limitCharactersPage)

        return {
            "characters": [character.to_dict() for character in characters],
            "totalPages": totalPages,
            "currentPage": page
        }

    def get_by_id(self, character_id):
        character = self.character_repository.get_by_id(character_id)

        if character:
            return character.to_dict()
        else:
            return None
