import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("Received:", message.payload.decode())

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883)
client.subscribe("lab/12114875/temperature")

client.loop_forever()
