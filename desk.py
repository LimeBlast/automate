import json
import sys

from slackclient import SlackClient

import settings


def main():
    sc = SlackClient(settings.SLACK_API_TOKEN_FOXSOFT)

    print("Setting status")
    result = sc.api_call(
        "users.profile.set",
        user=settings.SLACK_USER_FOXSOFT,
        profile=json.dumps({
            "status_text": "At my desk",
            "status_emoji": ":desktop_computer:"
        })
    )
    print(result)

    # http://stackoverflow.com/a/23452742/1049688
    sys.stdout.flush()


if __name__ == '__main__':
    main()
