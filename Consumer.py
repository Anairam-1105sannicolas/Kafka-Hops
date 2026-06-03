from confluent_kafka import Consumer


config = {
    'bootstrap.servers': '192.168.68.59:9094',
    'group.id': 'kafka1',
    'auto.offset.reset': 'earliest',
}

topic = 'factory'
consumer = Consumer(config)
consumer.subscribe([topic])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Error:", msg.error())
        continue
    val = msg.value().decode('utf-8')
    print("Recibed Val", val)



consumer.close()