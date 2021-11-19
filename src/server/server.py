from flask_restplus import Api
from flask import Flask
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property


class Server():

    def __init__(self,):
        self.flask = Flask(__name__)
        self.api = Api(self.flask,
                       version="1.0",
                       title="Learnig Api",
                       description="Api simples criada como caso de estudo ou objecto de estudo",
                       doc="./doc"
                       )

    def run(self):
        """ Start a server"""

        self.api.run(debug=True)


server = Server()
