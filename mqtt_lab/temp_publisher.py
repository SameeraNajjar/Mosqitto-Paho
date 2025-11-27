import paho.mqtt.client as mqtt
import time
import random

broker = "localhost"  # Use "localhost" if Mosquitto is running locally
topic = "lab/12114875/temperature"

client = mqtt.Client()
client.connect(broker)

while True:
    temp = random.randint(20, 35)
    message = f"ID=12114875, Temperature={temp}"
    print("Publishing:", message)
    client.publish(topic, message)
    time.sleep(3)
