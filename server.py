import json
import flask
from flask import Flask, request
from flask_restful import Resource, Api

import formpars

class Signer(Resource):
    def post(self, pin: int):
        # TODO: db logic
        return {}

class User(Resource):
    def post(self, pin:int, id: int, pic_name: str):
        # TODO: save into db
        return {}

class Vocabulary(Resource):
    def get(self, pin: int):
        return formpars.get_vocabulary()


def main():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Signer, '/game/<int:pin>/sign')
    api.add_resource(User, '/game/<int:pin>/<int:id>/<string:pic_name>')
    api.add_resource(Vocabulary, '/game/<int:pin>/vocabulary')

    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
