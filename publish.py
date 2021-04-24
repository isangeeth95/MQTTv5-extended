import paho.mqtt.publish as publish

publish.single("house/main-light", "OFF", hostname="10.0.2.4")
