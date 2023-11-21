from database.db import db

class QueryComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    queryId = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __init__(self, queryId, username, description):
        self.queryId = queryId
        self.username = username
        self.description = description