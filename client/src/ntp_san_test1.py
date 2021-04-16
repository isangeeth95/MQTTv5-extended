#import client as mqtt #import the client1

from paho.mqtt import client as mqtt
#import paho.mqtt.client as mqtt

broker_address="192.168.56.111" 
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("SAN1") #create new instance
#client.connect(broker_address) #connect to broker
client.ntp_san(broker_address)
client.publish("house/main-light","OFF")#publish
