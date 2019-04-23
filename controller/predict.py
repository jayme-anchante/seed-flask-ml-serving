# external
from flask import request
from flask_restful import Resource
# custom
from services.services import Pipeline
from helpers.disk import load_from_disk
from helpers.disk import get_latest_model


class Predict(Resource):
    @staticmethod
    def post():
        data_json = request.data.decode("utf-8")
        pipeline = load_from_disk(filename=get_latest_model())
        predictions = pipeline.predict(data_json)
        return predictions
