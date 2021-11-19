from flask import Flask
from flask_restplus import Api


class Server:

    def __init__(self,):
        self.flask = Flask(__name__)
        self.api = Api(self.flask,
                       version="1.0",
                       title="Learnig Api",
                       description="Api simples criada como caso de estudo ou objecto de estudo",
                       doc="/doc"
                       )

    def run(self, ):
        """ Start a server"""

        self.flask.run(debug=True)
