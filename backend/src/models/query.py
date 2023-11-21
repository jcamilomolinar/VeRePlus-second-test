from database.db import db

class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    birthTable = db.Column(db.String(255), nullable=False)
    avgAgeMother = db.Column(db.Boolean(), nullable=False)
    avgBirthWeight = db.Column(db.Boolean(), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    year = db.Column(db.String(255), nullable=False)

    def __init__(self, name, username, description, birthTable, avgAgeMother, avgBirthWeight, state, year):
        self.name = name
        self.username = username
        self.description = description
        self.birthTable = birthTable
        self.avgAgeMother = avgAgeMother
        self.avgBirthWeight = avgBirthWeight
        self.state = state
        self.year = year