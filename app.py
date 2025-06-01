from flask import Flask, jsonify
from src.models import db, ma
from config.settings import DATABASE_URI
from src.routes.characters_routes import characters_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)

app.register_blueprint(characters_bp, url_prefix='/characters')

if __name__ == "__main__":
  app.run(debug=True)