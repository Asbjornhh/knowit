import paho.mqtt.client as mqtt
import time

# MQTT broker details
BROKER = "localhost"
PORT = 1883
TOPIC = "test/topic"

# Callback when a message is received
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

# Set up the subscriber
subscriber = mqtt.Client("PythonSubscriber")
subscriber.connect(BROKER, PORT)
subscriber.subscribe(TOPIC)
subscriber.on_message = on_message

# Start the subscriber loop
subscriber.loop_start()

# Set up the publisher
publisher = mqtt.Client("PythonPublisher")
publisher.connect(BROKER, PORT)
time.sleep(1)  # Give it a short delay to ensure the connection is established

# Keep the script running and send a different message every 3 seconds
message_count = 0
try:
    while True:
        message = f"Jarle e Gay {message_count}gonge "
        publisher.publish(TOPIC, message)
        print(f"Sent: {message}")
        message_count += 1
        time.sleep(0.00001)
except KeyboardInterrupt:
    print("Exiting...")
    subscriber.loop_stop()
    subscriber.disconnect()
    publisher.disconnect()
