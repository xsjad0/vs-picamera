import paho.mqtt.client as mqtt
import json
import os
import logging
from manager import Manager


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


logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
logger = logging.getLogger("[pi-camera]")

# read config file
config_mqtt = ''
with Manager('config.json', 'r') as config_file:
    config_mqtt = json.load(config_file)['mqtt']
logger.debug("config.json loaded")

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
