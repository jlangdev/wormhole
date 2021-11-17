from flask import Flask
from flask import request
import json
import requests
import socket


def create_app():
    app = Flask(__name__)

    @app.route('/test', methods=['POST'])
    def test():
        print(request.json)
        return "thanks"
    return app

app = create_app().run(host='0.0.0.0', port=8000, debug=True)
