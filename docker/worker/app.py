
#                      __                 
# __  _  _____________|  | __ ___________ 
# \ \/ \/ /  _ \_  __ \  |/ // __ \_  __ \
#  \     (  <_> )  | \/    <\  ___/|  | \/
#   \/\_/ \____/|__|  |__|_ \\___  >__|   
#                          \/    \/       
from flask import Flask
from flask import request
import json
import requests
import socket



def get_host_info():
    hostname = socket.gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    addr = s.getsockname()[0]
    s.close()
    hostinfo = {'name': hostname, 'addr': addr}
    return hostinfo

def write_and_run(lines):
    with open('payload.py', 'w') as f:
        for line in lines:
            f.write(line)
        f.close()

    exec(open("payload.py").read())
    
def create_app():
    app = Flask(__name__)

    @app.route('/do', methods=['POST'])
    def do():
        print(request.json)
        lines = request.json['file']
        write_and_run(lines)
        response = {
            "host": hostinfo,
            "lines": lines
        }
        return response

    @app.route('/info', methods=['GET'])
    def info():
        return hostinfo
    return app

discover = "http://host.docker.internal:5000/discover"
#discover = "http://localhost:5000/discover"
hostinfo = get_host_info()
requests.post(url=discover, json=hostinfo)
app = create_app()

#app = create_app().run(host='0.0.0.0', port=5001, debug=True)



