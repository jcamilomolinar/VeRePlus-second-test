from flask import Blueprint, request
from utils.querycreator import querycreator
from database.bigquery import searchData
from models.query import Query
from database.db import db
querydata = Blueprint('querydata', __name__)

# Create the route for the form data endpoint here and return the data from the database as JSON data in the response body
@querydata.route('/api/send-data', methods=['POST'])
def receiveQueryData():
    # Get the data from the request
    data = request.get_json()

    # Save the query if the user wants to
    if data['saveQuery']:
        saveQueryData(data)

    # Create the query
    query = querycreator(data)

    # Get the data from the database
    records = searchData(query)

    # Return the data
    return records


# Save the form data to the database 
def saveQueryData(data):
    # Create the query object
    new_query = Query(
        data['queryName'], 
        data['username'], 
        data['queryDescription'],
        data['birthTable'],
        data['avgAgeMother'],
        data['avgBirthWeight'],
        data['state'],
        data['year']
        )

    # Save the query to the database
    db.session.add(new_query)
    db.session.commit()