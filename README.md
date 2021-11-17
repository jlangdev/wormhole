```
                            .__           .__          
__  _  _____________  _____ |  |__   ____ |  |   ____  
\ \/ \/ /  _ \_  __ \/     \|  |  \ /  _ \|  | _/ __ \ 
 \     (  <_> )  | \/  Y Y  \   Y  (  <_> )  |_\  ___/ 
  \/\_/ \____/|__|  |__|_|  /___|  /\____/|____/\___  >
                          \/     \/                 \/ 
```
## Description

Wormhole is an environment for scalable, parallel execution of python scripts in Docker containers. This multi-container Docker application stands up a wormhole server and an arbitrary number of workers. As workers are created, they automatically post their hostname and address to the wormhole which stores them in a list. After creating a payload, send_it forwards the file to the wormhole. The wormhole iterates through its list of hosts and forwards the payload to each worker. Upon receiving the payload, each worker will write the file to disk and then execute it in parallel.

## Installation

requirements:
- Docker
- Docker Compose
- Flask
- Python 3

Install with git
```
$ git clone <repo>
```
## Usage
First, stand up the environment with docker compose.

```
$ cd docker
$ docker compose build
$ docker compose up --scale worker=10
```

Once that's working, the environment is set up and we can create a payload. This example uses test_server.py and payload.py from the examples folder for proof of concept. Upon execution of forwarder.py, the requests should show up in test_server's terminal output.

Create a payload. The file name doesn't matter, but in this example I use payload.py

```
#example payload
import requests
requests.post(url="http://host.docker.internal:8000/test", json={'msg':"operational wormhole"})
```

Navigate to the examples directory and launch the example flask app on port 8000

```
$ cd example
$ python3 test_server.py
```

Now that we have a payload and a server to prove it, we can actually run the forwarder to bulk-execute the script

```
python3 send_it.py --file payload.py
```
The test server's output should reflect successful execution.
```
{'msg': 'operational wormhole'}
127.0.0.1 - - [16/Nov/2021 21:29:09] "POST /test HTTP/1.1" 200 -
{'msg': 'operational wormhole'}
127.0.0.1 - - [16/Nov/2021 21:29:09] "POST /test HTTP/1.1" 200 -
{'msg': 'operational wormhole'}
127.0.0.1 - - [16/Nov/2021 21:29:09] "POST /test HTTP/1.1" 200 -
{'msg': 'operational wormhole'}
...
```