from flask import request, jsonify
from flask_restful import Resource
from Model import db, Results, ResultsSchema

result_schema = ResultsSchema()
results_schema = ResultsSchema(many=True)

class ResultsResource(Resource):
    def get(self):
        all_results = Results.query.all()
        query_out = results_schema.dump(all_results)
        return jsonify(query_out)

