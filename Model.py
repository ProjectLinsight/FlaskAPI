from flask import Flask, request, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#Init DB
db = SQLAlchemy()
ma = Marshmallow()

#Results Class
class Results(db.Model):
    __tablename__ ='results'
    id = db.Column(db.BigInteger, primary_key=True)
    index = db.Column(db.String(255))
    grade = db.Column(db.String(255))
    subjectCode = db.Column(db.String(255))
    batch = db.Column(db.String(255))
    yoe = db.Column(db.String(255))
    semester = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __init__(self,index,grade,subjectCode,batch,yoe,semester,created_at,updated_at):
        self.index = index
        self.grade = grade
        self.subjectCode = subjectCode
        self.batch = batch
        self.yoe = yoe
        self.semester = semester
        self.created_at = created_at
        self.updated_at = updated_at
    
class ResultsSchema(ma.Schema):
    class Meta:
        fields = ('id','index','grade','subjectCode','batch','yoe','semester','created_at','updated_at')
