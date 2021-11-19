from src.server import Server
from flask_restplus import Api, Resource
from flask import Flask
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property


app, api = Server.app, Server.api

books_db = [
    {"id": 0, "title": "War and peace"},
    {"id": 1, "title": "Clean code"},
]


@api.route('/books', methods=['GET'])
class BookList(Resource):
    """ Return book list """

    def get(self, ):
        return books_db
