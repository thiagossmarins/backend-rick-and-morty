from flask import Flask, jsonify
from src.models import db
from config.settings import DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def hello_wold():
  return jsonify({
    "hello": "wold"
  }
  )

if __name__ == "__main__":
  app.run(debug=True)