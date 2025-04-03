import json
from confluent_kafka import Producer
from dateparser import parse
from websockets.sync.client import connect


def consume():
    producer = Producer({"bootstrap.servers": "kafka:9092"})
    product_ids = ["BTC-USD"]

    with connect("wss://ws-feed.exchange.coinbase.com") as websocket:
        subscription_message = {
            "type": "subscribe",
            "channels": [
                {
                    "name": "ticker",
                    "product_ids": product_ids,
                }
            ],
        }

        websocket.send(json.dumps(subscription_message))

        while True:
            message = json.loads(websocket.recv())

            if message["type"] == "ticker":
                _format_date(message)
                producer.produce(
                    "ticker",
                    json.dumps(message).encode("utf-8"),
                )


def _format_date(message: dict):
    message["time_ms"] = parse(message["time"]).timestamp() * 1000


if __name__ == "__main__":
    consume()
