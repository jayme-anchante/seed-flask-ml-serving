# core
import os
# external
import flask_restful
from flask import Flask
from dotenv import load_dotenv, find_dotenv
# custom
from controller.fit import Fit
from controller.predict import Predict
from controller.delete import Delete
load_dotenv(find_dotenv())


app = Flask(__name__)
api = flask_restful.Api(app)
api.add_resource(Fit, "/fit")
api.add_resource(Predict, "/predict")
api.add_resource(Delete, "/delete")

if __name__ == "__main__":
    host = os.getenv("HOST")
    port = int(os.getenv("PORT"))
    app.run(host=host, port=port)
