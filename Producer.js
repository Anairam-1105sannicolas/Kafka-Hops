const { Kafka } = require("kafkajs");

// 1. Initialize Kafka client
const kafka = new Kafka({
  clientId: "my-app",
  brokers: ["10.25.233.148:9092"], // Replace with your broker addresses
});

// 2. Create producer instance
const producer = kafka.producer();

// 3. Connect and send messages
const runProducer = async () => {
  try {
    await producer.connect();
    
    // Send a message to the "my-topic" topic
    await producer.send({
      topic: "factory",
      messages: [
        { value: "sensor reading" },
        { key: "Sensor1", value: JSON.stringify({ name: "Test", timestamp: Date.now() }) }
      ],
    });
    
    console.log("Message sent successfully");
  } catch (error) {
    console.error("Error sending message:", error);
  } finally {
    await producer.disconnect();
  }
};

runProducer();   