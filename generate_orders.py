#!/usr/bin/env python3

from kafka import KafkaProducer
from kafka.errors import KafkaError

import datetime
import random
import json
import time


PRODUCTS = [
    {"type": "car", "brand": "Ford", "product": "Falcon XR6"},
    {"type": "car", "brand": "Ford", "product": "Falcon XR8"},
    {"type": "car", "brand": "Holden", "product": "Commodore Tourer"},
    {"type": "food", "brand": "Safeway", "product": "Celery"},
    {"type": "food", "brand": "Heinz", "product": "Tomato Sauce"},
    {"type": "food", "brand": "Melbourne Hotsauce Company", "product": "Bum Burner"},
    {"type": "tv", "brand": "Panasonic", "product": "65 4K HDR OLED TV"},
    {"type": "tv", "brand": "Samsung", "product": "98 QLED 8K UHD TV"},
    {"type": "tv", "brand": "LG", "product": "65 OLED TV"},
    {"type": "spirits", "brand": "Laphroaig", "product": "10YO Single Malt Whisky"},
    {"type": "spirits", "brand": "Ardbeg", "product": "Uigeadail"},
    {"type": "spirits", "brand": "Bruichladdich", "product": "Sherry Cask Edition 25YO"},
]


def generate_items(choices=3):
    return [random.choice(PRODUCTS) for _ in range(random.randrange(1, choices + 1))]

def generate_order(order_id):
    return {
        "order_id": order_id,
        "order_time": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z"),
        "items": generate_items(),
    }

def send_items_forever(producer, topic):
    order_id = 1

    while True:
        order = generate_order(order_id)
        producer.send(topic, key=order_id, value=order)
        print(order)
        order_id += 1

        time.sleep(random.randrange(5))

if __name__ == "__main__":
    brokers = ["kafka-1:9092", "kafka-2:9092", "kafka-3:9092"]

    producer = KafkaProducer(
        bootstrap_servers=brokers,
        value_serializer=lambda m: json.dumps(m).encode('utf-8'),
    )

    send_items_forever(producer, "orders")
