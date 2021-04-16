import paho.mqtt.client as mqtt
import time

broker="192.168.56.111"
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
client = mqtt.Client("python1")
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
print("publishing")
#ret=client.publish("house/bulb1", "Test message 0", 0)
#print("published return=",ret)
#time.sleep(3)
ret=client.auth("abcnethmi", "123", "payload1")
print("authenticate return=",ret)






