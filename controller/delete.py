# external
from flask_restful import Resource
# custom
from helpers.disk import delete_all_except_latest


class Delete(Resource):
    @staticmethod
    def delete():
        delete_all_except_latest()
        return "Deleted all models except latest"
