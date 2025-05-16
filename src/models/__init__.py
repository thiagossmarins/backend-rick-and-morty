from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

from src.models.characters_model import *
from src.models.locations_model import *
from src.models.episodes_model import *
from src.models.characters_episodes_model import *