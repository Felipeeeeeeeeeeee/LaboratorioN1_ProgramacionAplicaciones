from utils.db import db

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100))
    
    def __init__(self, content):
        self.content = content