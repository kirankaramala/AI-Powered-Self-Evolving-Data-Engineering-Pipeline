from kafka import KafkaConsumer
import json
import pandas as pd
from streaming.parser import DebeziumParser


def consume_stream():

    consumer = KafkaConsumer(
        "dbserver1.testdb.orders_stream",
        bootstrap_servers="localhost:9093",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="capstone-group",
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )

    print("Waiting for Kafka messages...\n")

    for message in consumer:

        parsed = DebeziumParser.parse(message.value)

        df = pd.DataFrame([parsed])

        yield df