import sys
import json


def main(input):
    # print("raw: "+input)
    # payload = json.loads(input)
    # print("json: "+str(payload))
    # print("actor: "+payload['actor'])

    # return "Hello "+payload['actor']+"!"
    open("test.txt", "w").write("test")
    payload = {
        "action": "edited",
        "actor": "jeffrey-sentry",
        "new_tags": [
        "debugtoolbar",
        "tag-production"
        ],
        "repo": "getsentry/spotlight",
        "tags": [
        "debugtoolbar",
        "tag-to-be-production-20231114"
        ]
    }

    message = f"[{payload['repo']}](https://github.com/{payload['repo']}) was moved to {payload['tags'][0]} from {payload['tags'][0]} by @{payload['actor']}."
    message += f"\n\n {payload['actor']}please review the changes for security-as-code terraform file."

    if True:
        message += "\n\n ❗ ❗ ❗  **A `tf state rm` will be require before PR is merged**❗ ❗ ❗ "
    return message


if __name__ == '__main__':
    print(main(sys.argv[1]))