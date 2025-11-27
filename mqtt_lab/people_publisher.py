import paho.mqtt.client as mqtt
import time
import random

broker = "localhost"
topic = "lab/12114875/people"

client = mqtt.Client()
client.connect(broker)

while True:
    people = random.randint(0, 10)
    message = f"ID=12114875, PeopleCount={people}"
    print("Publishing:", message)
    client.publish(topic, message)
    time.sleep(3)
