from confluent_kafka import Consumer


config = {
    'bootstrap.servers': 'localhost:9092',
    'acks': 'all',
    'group.id': 'kafka1',
    'auto.offset.reset': 'earliest',
}

topic = 'factory'
consumer = Consumer(config)
consumer.subscribe([topic])

while True:
    msg = consumer.poll(1.0)

    if (msg is None):
        print("Message is None")
    else:
        val = msg.value().decode('utf-8')
        print("Recibed Val", val)



consumer.close()