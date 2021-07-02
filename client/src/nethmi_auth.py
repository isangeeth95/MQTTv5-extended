import paho.mqtt.client as mqtt
from paho.mqtt import properties as Properties
from paho.mqtt import packettypes as PacketTypes
import time

broker="192.168.78.156"
port =1883

def on_log(client, userdata, level, buf):
    print(buf)

#def on_connect(client, userdata, flags, rc):
#    if rc==0:
#        client.connected_flag=True
#        print("connected ok")
#    else:
#        print("Bad connection Returned code=",rc)
#        client.loop_stop()

#def on_disconnect(client, userdata, rc):
#    print("client disconnected ok")

#def on_auth(client, userdata, mid):
#    print("In on_auth callback mid=", mid)

#mid.Client.connected_flag=False
client = mqtt.Client("python2")
client.on_log=on_log
#client.on_connect = on_connect
#client.on_disconnect = on_disconnect
#client.on_auth = on_auth
client.connect(broker, port)
#client.loop_start()
#while not client.connected_flag:
#    print("in wait loop")
#    time.sleep(1)
#time.sleep(3)
#print("publishing")
#ret=client.publish("house/bulb1", "Test message 0", 0)
#print("published return=",ret)
#time.sleep(3)

#ret=client.auth("abcnethmi", "123")
#print("authenticate return=",ret)


#san=Properties.Properties(PacketTypes)
#publish_properties = Properties.Properties(PacketTypes.PacketTypes.PUBLISH)
#print("sangeeth:  ",PacketTypes.PacketTypes.AUTH)
#print(publish_properties)
#publish_properties.UserProperty = ("a", "2")
#publish_properties.UserProperty = ("c", "3")
#ret=client.auth("credentials", properties=publish_properties)
#ret=client.publish("house/bulb1", "Test message 0", properties=publish_properties)
#print("published return=",ret)


auth_properties = Properties.Properties(PacketTypes.PacketTypes.AUTH)
print("sangeeth:  ",PacketTypes.PacketTypes.AUTH)
print(auth_properties)
auth_properties.UserProperty = ("username", "user")
auth_properties.UserProperty  = ("password", "pass")
ret=client.auth("authdata", "123", properties=auth_properties)
print("properties_auth: ", auth_properties)
print("authenticate return=",ret)












