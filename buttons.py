import paho.mqtt.client as mqtt
import settings
import sys


def on_publish(client, userdata, mid):
    print("Message " + str(mid) + " published.")


def main():
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(settings.MQTT_USERNAME, settings.MQTT_PASSWORD)
    mqtt_client.connect(settings.MQTT_HOST, int(settings.MQTT_PORT))
    mqtt_client.on_publish = on_publish

    topic = "buttons/{}".format(str(sys.argv[1]))
    payload = 'on'

    mqtt_client.publish(topic, payload, retain=False)


if __name__ == '__main__':
    main()
