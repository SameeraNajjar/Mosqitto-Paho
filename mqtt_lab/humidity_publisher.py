import paho.mqtt.client as mqtt
import time
import random

broker = "localhost"
topic = "lab/12114875/humidity"

client = mqtt.Client()
client.connect(broker)

while True:
    hum = random.randint(30, 70)
    message = f"ID=12114875, Humidity={hum}"
    print("Publishing:", message)
    client.publish(topic, message)
    time.sleep(3)
