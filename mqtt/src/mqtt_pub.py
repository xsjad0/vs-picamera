import sys
import os
import getopt
import logging
import json
from manager import Manager
import paho.mqtt.publish as publish
from picamera import PiCamera

logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
logger = logging.getLogger("[mqtt_pub]")

app_path = os.path.abspath(os.getcwd())


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hc:', ['help', 'command='])
    except getopt.GetoptError as e:
        print(str(e))
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if (opt in ('-h', '--help')):
            usage()
            sys.exit()
        elif (opt in ('-c', '--command')):
            try:
                commands[arg]()
                sys.exit()
            except KeyError as e:
                print(str(e))
                sys.exit(2)

    usage()


def capture():
    logger.info('capture')
    pub('capture')


def video_start():
    logger.info('start video')
    pub('video_start')


def video_stop():
    logger.info('stop video')
    pub('video_stop')


def delete():
    logger.info('delete storage')
    pub('delete')


def pub(payload):
    config = ''
    with Manager('config.json', 'r') as config_file:
        config = json.load(config_file)['mqtt']

    publish.single(
        config['topic'], payload='{\'cmd\':\'' + str(payload) + '\'}', hostname=config['broker'], port=config['port'], keepalive=config['keep_alive']
    )


def usage():
    print('usage: mqtt_pub.py -c <capture/video_start/video_stop/delete>')


if __name__ == "__main__":
    commands = {
        'capture': capture,
        'video_start': video_start,
        'video_stop': video_stop,
        'delete': delete
    }

    main()
