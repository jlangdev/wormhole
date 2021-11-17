
#                             .__           .__          
# __  _  _____________  _____ |  |__   ____ |  |   ____  
# \ \/ \/ /  _ \_  __ \/     \|  |  \ /  _ \|  | _/ __ \ 
#  \     (  <_> )  | \/  Y Y  \   Y  (  <_> )  |_\  ___/ 
#   \/\_/ \____/|__|  |__|_|  /___|  /\____/|____/\___  >
#                           \/     \/                 \/ 
from flask import Flask
from flask import request
import json
import requests
import socket


def create_app():
    app = Flask(__name__)

    @app.route('/wormhole', methods=['POST'])
    def wormhole():
        print(request.json)
        responses = []
        for worker in workers:
            url = "http://" + worker['addr'] + ":5000/do"
            print(url)
            r = requests.post(url=url, json=request.json)
            responses.append(r.json)
        return str(responses)

    @app.route('/discover', methods=['POST'])
    def discover():
        host=request.json
        workers.append(host)
        return "hosts"
    
    @app.route('/hosts', methods=['GET'])
    def hosts():
        return str(workers)
    return app
    
workers =  []
app = create_app()
#app = create_app().run(host='0.0.0.0', port=5000, debug=True)
