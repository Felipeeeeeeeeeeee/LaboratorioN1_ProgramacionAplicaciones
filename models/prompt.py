from utils.db import db
from datetime import datetime
from pytz import timezone

class Prompt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.now(timezone('America/Santiago')))

    def __init__(self, content):
        self.content = content
