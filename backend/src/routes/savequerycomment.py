from flask import Blueprint, request
from models.querycomment import QueryComment
from database.db import db
savequerycomment = Blueprint('savequerycomment', __name__)

# Save the form data to the database 
@savequerycomment.route('/api/send-comment-data', methods=['POST'])
def saveQueryData():
    data = request.get_json()
    # Create the query object
    new_query = QueryComment(
        data['queryId'],
        data['username'], 
        data['commentDescription']
        )
    
    # Save the query to the database
    db.session.add(new_query)
    db.session.commit()
    return 'Data received', 200