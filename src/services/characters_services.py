from src.models.characters_model import Characters
from src.repositories.characters_repositories import CharacterRepositories
import math

class CharacterService():
  def __init__(self):
    self.character_repository = CharacterRepositories()

  def getAllCharacters(self, page, term=None):
    limitCharactersPage = 20;
    offset = (page - 1) * limitCharactersPage;

    characters, total = self.character_repository.getAllCharacters(
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