import requests
requests.post(url="http://host.docker.internal:8000/test", json={'msg':"operational wormhole"})
#requests.post(url="http://localhost:8000/test", json={'msg':"operational wormhole"})