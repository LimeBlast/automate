import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SLACK_API_TOKEN_BRUMTECH = os.environ.get("SLACK_API_TOKEN_BRUMTECH")
SLACK_API_TOKEN_FOXSOFT = os.environ.get("SLACK_API_TOKEN_FOXSOFT")
SLACK_USER_BRUMTECH = os.environ.get("SLACK_USER_BRUMTECH")
SLACK_USER_FOXSOFT = os.environ.get("SLACK_USER_FOXSOFT")

MQTT_USERNAME = os.environ.get("MQTT_USERNAME")
MQTT_PASSWORD = os.environ.get("MQTT_PASSWORD")
MQTT_HOST = os.environ.get("MQTT_HOST")
MQTT_PORT = os.environ.get("MQTT_PORT")
