from paho.mqtt import timesync as timesync

timesync.single(hostname="10.0.2.9", client_id="san")
