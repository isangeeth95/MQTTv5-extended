import paho.mqtt.client as mqtt
from paho.mqtt import properties as Properties
from paho.mqtt import packettypes as PacketTypes
import time
import hashlib,binascii,os
import sys

#broker="192.168.1.107"
broker = "10.0.2.9"
port =1883

def on_log(client, userdata, level, buf):
    print(buf)


client = mqtt.Client("python2")
client.on_log=on_log
client.connect(broker, port)


def hash_password(hash_password):
    salt  = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

auth_properties = Properties.Properties(PacketTypes.PacketTypes.AUTH)
print("sangeeth:  ",PacketTypes.PacketTypes.AUTH)

print(auth_properties)


#auth_properties.UserProperty = ("username", "admin")
#password = "password"

auth_properties.UserProperty = ("username", "wrong")
password = "wrongpassword"


auth_properties.UserProperty  = ("password", hash_password(password))


ret=client.auth("authdata", "123", properties=auth_properties)
print("properties_auth: ", auth_properties)
print("authenticate return=",ret)












