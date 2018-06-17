
import json
from flask import request, abort, render_template
import flask_restful as restful
from flask.ext.restful import reqparse
from flask_rest_service import app, api, mongo
from bson.objectid import ObjectId


class ReadingList(restful.Resource):
    def __init__(self, *args, **kwargs):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('testing', type=str)
        super(ReadingList, self).__init__()

    def get(self):
        return  [x for x in mongo.db.testFeed.find()]

    def post(self):
        args = self.parser.parse_args()
        if not args['testing']:
            abort(400)

        jo = json.loads(args['testing'])
        test_id = mongo.db.testFeed.insert(jo)
        return mongo.db.testFeed.find_one({"_id": test_id})


class Reading(restful.Resource):
    def get(self, test_id):
        return mongo.db.testFeed.find_one_or_404({"_id": test_id})

    def delete(self, test_id):
        mongo.db.testFeed.find_one_or_404({"_id": test_id})
        mongo.db.testFeed.remove({"_id": test_id})
        return '', 204



class Root(restful.Resource):
    def get(self):
        return {
            'status': 'OK',
            'mongo': str(mongo.db),
        }


class Add(restful.Resource):
    def get(self):
        return {
            'status': 'OK',
            'mongo': str(mongo.db),
        }

api.add_resource(Root, '/')
api.add_resource(ReadingList, '/testFeed/')
api.add_resource(Reading, '/testFeed/<ObjectId:test_id>')