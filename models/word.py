from utils.db import db

class Word(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    count = db.Column(db.Integer, default=0)
