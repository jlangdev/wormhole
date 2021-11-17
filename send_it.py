#                           .___    .__  __   
#   ______ ____   ____    __| _/    |__|/  |_ 
#  /  ___// __ \ /    \  / __ |     |  \   __\
#  \___ \\  ___/|   |  \/ /_/ |     |  ||  |  
# /____  >\___  >___|  /\____ |_____|__||__|  
#      \/     \/     \/      \/_____/           
import requests
import json
import argparse


wormhole = "http://localhost:5000/wormhole"

def read_file(file):
    lines = []
    with open(file) as f:
        lines = f.readlines()
    return lines

def main():
    lines = read_file(file)
    data={'file': lines}
    print(data)
    r = requests.post(url=wormhole, json=data)
    return r.text

parser = argparse.ArgumentParser(
    description="Wormhole"
)

parser.add_argument(
    '-f', '--file',
    help="Python file to send via wormhole", required=True
)
args = parser.parse_args()
file = args.file

if __name__ == "__main__":
    """
    Start the main routine
    """
    main()