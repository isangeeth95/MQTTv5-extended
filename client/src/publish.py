from paho.mqtt import publish as publish

publish.single("house/main-light", "OFF", hostname="10.0.2.9", client_id="san")
