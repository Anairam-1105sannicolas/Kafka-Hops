const { Kafka } = require("kafkajs");

// 1. Initialize Kafka client
const kafka = new Kafka({
  clientId: "my-app",
  brokers: ["192.168.68.59:9094"],
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
        { value: "texto 123" }
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