
import os
from flask import Flask, request, jsonify
import flask_restful as restful
from flask.ext.pymongo import PyMongo
from flask import make_response, render_template
from bson.json_util import dumps
import json
import urllib

MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "mongodb://the-wire:" + urllib.parse.quote("Success@1996") + "@ds061076.mlab.com:61076/feed-db"

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URL
mongo = PyMongo(app, config_prefix="MONGO")


@app.route('/', methods=['GET'])
def form():
    # database status
    root = flask_rest_service.resources.Root()
    root_test = flask_rest_service.resources.Root.get(root)

    return render_template('form.html', db_status=root_test)

@app.route('/all', methods=['GET'])
def retrieve_all_meanings():
    test = flask_rest_service.resources.ReadingList()
    test_read = flask_rest_service.resources.ReadingList.get(test)
    # test_read[0]['_id'] = 'null'
    print(dumps(test_read))
    return jsonify({'output' : json.loads(dumps(test_read))})

def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api = restful.Api(app)
api.representations = DEFAULT_REPRESENTATIONS

import flask_rest_service.resources
