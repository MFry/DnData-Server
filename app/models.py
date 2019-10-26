from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True)
    characters = db.relationship('Character', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.name}>'


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    name = db.Column(db.String(128))
    link = db.Column(db.String(128))
    character_class = db.Column(db.String(128))
    character_race = db.Column(db.String(128))


class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    characters = db.relationship('Character', backref="campaign", lazy='dynamic')