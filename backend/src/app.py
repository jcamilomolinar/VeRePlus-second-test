from flask import Flask
from flask_cors import CORS
from routes.querydata import querydata
from routes.querycrud import querycrud
from routes.savequerycomment import savequerycomment
from database.db import init_app

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/babysearch'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_app(app)

app.register_blueprint(querydata)
app.register_blueprint(querycrud)
app.register_blueprint(savequerycomment)