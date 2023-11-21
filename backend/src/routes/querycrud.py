from flask import Blueprint, request, jsonify
querycrud = Blueprint('querycrud', __name__)
from models.query import Query
from models.querycomment import QueryComment
from database.db import db

# Create the route for the form data endpoint here and return the data from the database as JSON data in the response body
@querycrud.route('/api/retrieve-query')
def retrieveQueryData():
    all_queries = Query.query.all()
    all_queries = [
        {
            'queryId': query.id,
            'queryName': query.name,
            'username': query.username,
            'queryDescription': query.description,
            'birthTable': query.birthTable,
            'avgAgeMother': query.avgAgeMother,
            'avgBirthWeight': query.avgBirthWeight,
            'state': query.state,
            'year': query.year
        } for query in all_queries
    ]
    return jsonify(all_queries)

# Create the route for the comment data for each query 
@querycrud.route('/api/retrieve-comment')
def retrieveQueryComment():
    all_comments = QueryComment.query.all()
    all_comments = [
        {
            'queryId': comment.id,
            'queryCommentId': comment.queryId,
            'username': comment.username,
            'commentDescription': comment.description,
        } for comment in all_comments
    ]
    return jsonify(all_comments)

# Create the route for the form data endpoint here and return the data from the database as JSON data in the response body
@querycrud.route('/api/retrieve-query/<int:id>')
def retrieveQueryDataById(id):
    query = Query.query.get(id)
    return {
        'birthTable': query.birthTable,
        'avgAgeMother': query.avgAgeMother,
        'avgBirthWeight': query.avgBirthWeight,
        'state': query.state,
        'year': query.year
    }

# Create the route for deleting a query by id
@querycrud.route('/api/delete-query/<int:id>', methods=['DELETE'])
def deleteQueryCommentById(id):
    query = Query.query.get(id)
    db.session.delete(query)
    db.session.query(QueryComment).filter(QueryComment.queryId == id).delete()
    db.session.commit()
    return jsonify('Query Deleted')