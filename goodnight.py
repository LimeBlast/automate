import time
import sys

import soco


def main():
    # examples taken from https://github.com/SoCo/SoCo/blob/master/examples/commandline/tunein.py
    tunein_service = 'SA_RINCON65031_'
    meta_template = """
    <DIDL-Lite xmlns:dc="http://purl.org/dc/elements/1.1/"
        xmlns:upnp="urn:schemas-upnp-org:metadata-1-0/upnp/"
        xmlns:r="urn:schemas-rinconnetworks-com:metadata-1-0/"
        xmlns="urn:schemas-upnp-org:metadata-1-0/DIDL-Lite/">
        <item id="R:0/0/0" parentID="R:0/0" restricted="true">
            <dc:title>{title}</dc:title>
            <upnp:class>object.item.audioItem.audioBroadcast</upnp:class>
            <desc id="cdudn" nameSpace="urn:schemas-rinconnetworks-com:metadata-1-0/">
                {service}
            </desc>
        </item>
    </DIDL-Lite>' """
    uri = 'x-sonosapi-stream:s51002?sid=254&flags=8224&sn=0'
    uri = uri.replace('&', '&amp;')
    meta = meta_template.format(title="Drone Zone", service=tunein_service)
    two_hours = 7200

    for device in soco.discover():
        if device.player_name == 'Master Bedroom':
            break
        else:
            device = None

    print("Controlling {}".format(device.player_name))

    print("Leaving any groups")
    device.unjoin()

    print("Setting volume")
    device.volume = 25

    print("Saying goodnight")
    device.play_uri('https://raw.githubusercontent.com/LimeBlast/automate/master/assets/goodnight.mp3')
    time.sleep(3)

    print("Playing Drone Zone")
    device.play_uri(uri, meta)

    print("Setting sleep timer")
    device.set_sleep_timer(two_hours)

    # http://stackoverflow.com/a/23452742/1049688
    sys.stdout.flush()


if __name__ == '__main__':
    main()
