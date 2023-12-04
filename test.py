import sys
import json


def main(input):
    payload = json.loads(input)
    print(payload)

if __name__ == '__main__':
    print(main(sys.argv[1]))