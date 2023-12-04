import sys
import json


def main(input):
    print("raw: "+input)
    payload = json.loads(input)
    print("json: "+str(payload))
    print("actor: "+payload['actor'])

if __name__ == '__main__':
    print(main(sys.argv[1]))