import json
import sys

from slackclient import SlackClient

import settings

sc = SlackClient(settings.SLACK_API_TOKEN_FOXSOFT)

print("Setting status")
result = sc.api_call(
    "users.profile.set",
    user=settings.SLACK_USER_FOXSOFT,
    profile=json.dumps({
        "status_text": "Armchair warrior",
        "status_emoji": ":seat:"
    })
)
print(result)

# http://stackoverflow.com/a/23452742/1049688
sys.stdout.flush()
