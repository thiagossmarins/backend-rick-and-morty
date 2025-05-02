from flask import Blueprint, jsonify
from src.controllers.characters_controller import CharactersController

characters_bp = Blueprint('characters_bp', __name__)
characters_controller = CharactersController()

@characters_bp.route('/', methods=['GET'])
def get_all_characters():
  return characters_controller.get_all_characters()

@characters_bp.route('/<int:character_id>', methods=['GET'])
def get_by_id(character_id):
    return characters_controller.get_by_id(character_id)