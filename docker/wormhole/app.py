
#                             .__           .__          
# __  _  _____________  _____ |  |__   ____ |  |   ____  
# \ \/ \/ /  _ \_  __ \/     \|  |  \ /  _ \|  | _/ __ \ 
#  \     (  <_> )  | \/  Y Y  \   Y  (  <_> )  |_\  ___/ 
#   \/\_/ \____/|__|  |__|_|  /___|  /\____/|____/\___  >
#                           \/     \/                 \/ 
from flask import Flask
from flask import request
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import http.client
import json
import requests
import socket
from itertools import repeat


#https://dev.to/rhymes/how-to-make-python-code-concurrent-with-3-lines-of-code-2fpe
def get_it(worker, json):
    try:
        url = "http://" + worker['addr'] + ":5000/do"
        r = requests.post(url=url, json=json)
        return r.json
    except socket.timeout:
        # in a real world scenario you would probably do stuff if the
        # socket goes into timeout
        pass

def create_app():
    app = Flask(__name__)

    @app.route('/wormhole', methods=['POST'])
    def wormhole():
        print(request.json)
        with PoolExecutor(max_workers=4) as executor:
            responses = list(executor.map(get_it, workers, repeat(request.json)))
        # for worker in workers:
        #     url = "http://" + worker['addr'] + ":5000/do"
        #     print(url)
        #     r = requests.post(url=url, json=request.json)
        #     responses.append(r.json)
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
