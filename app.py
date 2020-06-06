from flask import Flask, Blueprint
from flask_restful import Api
from resources.Results import ResultsResource
import os

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
#Routes
api.add_resource(ResultsResource, '/results')

# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# import os

# app = Flask(__name__)

# basedir = os.path.abspath(os.path.dirname(__file__))
# #Database
# app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:linsight37@localhost/linsight' 
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# #Init DB
# db = SQLAlchemy(app)
# ma = Marshmallow(app)

# #Results Class
# class Results(db.Model):
#     __tablename__ ='results'
#     id = db.Column(db.BigInteger, primary_key=True)
#     index = db.Column(db.String(255))
#     grade = db.Column(db.String(255))
#     subjectCode = db.Column(db.String(255))
#     batch = db.Column(db.String(255))
#     yoe = db.Column(db.String(255))
#     semester = db.Column(db.String(255))
#     created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
#     updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

#     def __init__(self,index,grade,subjectCode,batch,yoe,semester,created_at,updated_at):
#         self.index = index
#         self.grade = grade
#         self.subjectCode = subjectCode
#         self.batch = batch
#         self.yoe = yoe
#         self.semester = semester
#         self.created_at = created_at
#         self.updated_at = updated_at
    
# class ResultsSchema(ma.Schema):
#     class Meta:
#         fields = ('id','index','grade','subjectCode','batch','yoe','semester','created_at','updated_at')

# #Init Schema
# result_schema = ResultsSchema()
# results_schema = ResultsSchema(many=True)

# #Routes
# @app.route('/results',methods =['GET'])
# def get_results():
#     all_results = Results.query.all()
#     query_out = results_schema.dump(all_results)
#     return jsonify(query_out)

# if __name__ == '__main__':
#     app.run(debug=True)