var EventSource = require("eventsource");
const {Kafka} = require("kafkajs");

const url = "https://stream.wikimedia.org/v2/stream/recentchange";

const kafka = new Kafka({
  clientId: "wikievents",
  brokers: ["kafka:9092"],
});

const producer = kafka.producer();
const {Partitioners} = require('kafkajs')
kafka.producer({createPartitioner: Partitioners.DefaultPartitioner})

async function start() {
    await producer.connect();
    startEvents();
}

function startEvents() {
    console.log(`Connecting to EventStreams at ${url}`);
    let eventSource = new EventSource(url);
    eventSource.onopen = function () {
        console.log("--- Opened connection.");
    }
    eventSource.onerror = function (event) {
        console.error("--- Encountered error", event);
    };

    eventSource.onmessage = async function (event) {
        const data = JSON.parse(event.data);
        await producer.send({
            topic: "wikipedia-events",
            messages: [
                {
                    key: data.meta.id,
                    value: event.data,
                },
            ],
        });
    };

}


start();