#import paho.mqtt.subscribe as subscribe
from paho.mqtt import subscribe as subscribe

msg = subscribe.simple("house/main-light", hostname="10.0.2.4")
print("%s %s" % (msg.topic, msg.payload))
