from flask import Blueprint, jsonify
from src.controllers.characters_controller import CharactersController

characters_bp = Blueprint('characters_bp', __name__)
characters_controller = CharactersController()

@characters_bp.route('/', methods=['GET'])
def getAllCharacters():
  return characters_controller.getAllCharacters()