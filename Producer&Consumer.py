from confluent_kafka import Consumer, Producer

def delivery_callbaack(err, msg):
    if err:
        print(f'Message failed delivery: {err}')
    else:
        print(f'Message delivered to {msg.topic()}')


config_cons = {
    'bootstrap.servers': 'localhost:9092',
    'acks': 'all',
    'group.id': 'kafka1',
    'auto.offset.reset': 'earliest',
}

config_prod = {
    'bootstrap.servers': 'localhost:9092',
    'acks': 'all'
}

topic = 'factory'
consumer = Consumer(config_cons)
consumer.subscribe([topic])

producer = Producer(config_prod)
value = 'sensor reading'
key = 'Sensor 1'


while True:
    msg = consumer.poll(1.0)

    if (msg is None):
        print("Message is None")
    else:
        val = msg.value().decode('utf-8')
        print("Recibed Val", val)

        #reenvio
        producer.produce(topic, val, key, callback=delivery_callbaack)
        producer.poll(0)
        producer.flush()


consumer.close()