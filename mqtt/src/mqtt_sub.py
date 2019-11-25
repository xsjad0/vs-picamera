import paho.mqtt.client as mqtt
import json
import os
import logging
import sys
from time import sleep
from manager import Manager
from picamera import PiCamera


def on_connect(client, userdata, flags, rc):
    logger.debug("mqttc connected")
    logger.debug("result code: " + str(rc))
    mqttc.subscribe(config_mqtt['topic'])


def on_disconnect(client, userdata, rc):
    logger.debug("mqttc disconnected")


def on_subscribe(client, userdata, mid, granted_qos):
    logger.debug("mqttc subscribe on topic")


def on_unsubscribe(client, userdata, mid):
    logger.debug("mqttc unsubscribe from topic")


def on_message(client, userdata, msg):
    logger.info("mqtt message received")
    logger.info("topic: " + msg.topic)
    logger.info("msg: " + str(msg.payload))

    try:
        dict = json.loads(msg.payload.decode('utf-8'))
        for cmd in dict:
            commands[dict[cmd]]()
    except:
        logger.error("bad command")
        logger.error("sys_exc_info: " + sys.exc_info()[0])


def capture():
    logger.info("capture image")
    camera.start_preview()

    # camera warm-up time
    sleep(2)
    camera.capture(img_path)


def video_start():
    logger.info("start video recording")
    camera.start_recording(vid_path)


def video_stop():
    logger.info("stop video recording")
    camera.stop_recording()


def delete():
    logger.info("delete recorded files")
    os.remove(img_path)
    os.remove(vid_path)


logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
logger = logging.getLogger("[pi-camera]")

# store absolute path
app_path = os.path.abspath(os.getcwd())
img_path = app_path + '/../image/shot.jpg'
vid_path = app_path + '/../video/my_video.h264'

# read config file
config_mqtt = ''
with Manager('config.json', 'r') as config_file:
    config_mqtt = json.load(config_file)['mqtt']
logger.debug("config.json loaded")

commands = {
    'capture': capture,
    'video_start': video_start,
    'video_stop': video_stop,
    'delete': delete
}

# make PiCamera instance
camera = PiCamera(resolution=(1024, 768))

# make mqqt client
mqttc = mqtt.Client()

# register callback functions
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_subscribe = on_subscribe

# open connection
mqttc.connect(
    config_mqtt['broker'], config_mqtt['port'], config_mqtt['keep_alive']
)

# loop forever, block application
mqttc.loop_forever()
