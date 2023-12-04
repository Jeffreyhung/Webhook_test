import sys
import json


def main(input):
    # print("raw: "+input)
    # payload = json.loads(input)
    # print("json: "+str(payload))
    # print("actor: "+payload['actor'])

    # return "Hello "+payload['actor']+"!"

    message = "[getsentry/sentry](https://github.com/getsentry/sentry) "
    message += "was moved to tag-non-production from tag-production by @jeffreyhung.\n\n "
    message += "@jeffreyhung please review the changes for security-as-code terraform file."
    message += "\n\n ❗ ❗ ❗  ** A `tf state rm` will be require before PR is merged**❗ ❗ ❗ "
    return message


if __name__ == '__main__':
    print(main(sys.argv[1]))