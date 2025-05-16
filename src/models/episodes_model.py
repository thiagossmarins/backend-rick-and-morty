from src.models import db, ma

class Episodes(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    air_date = db.Column(db.String(50), nullable=True)
    episode = db.Column(db.String(20), nullable=True)

    characters = db.relationship('Characters', secondary='characters_episodes', back_populates='episodes')

    def __repr__(self):
        return f"<Episode {self.name}>"

class EpisodeOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    air_date = ma.String()
    episode = ma.String()