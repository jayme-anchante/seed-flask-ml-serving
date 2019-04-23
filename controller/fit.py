# external
from flask import request
from flask_restful import Resource
# custom
from services.services import Pipeline
from helpers.disk import save_to_disk


class Fit(Resource):
    @staticmethod
    def post():
        data_json = request.data.decode("utf-8")
        pipeline = Pipeline()
        pipeline.fit(data_json)
        save_to_disk(obj=pipeline)
        return "Model updated"
