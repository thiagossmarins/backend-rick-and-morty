from src.models import db, ma 

class CharactersEpisodes(db.Model):
    __tablename__ = 'characters_episodes'

    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), primary_key=True)

    def __repr__(self):
        return f"<CharactersEpisodes {self.character_id}>"