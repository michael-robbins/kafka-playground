#!/usr/bin/env python3

from kafka.admin import KafkaAdminClient, NewTopic


brokers = [
    "kafka-1:9092",
    "kafka-2:9092",
    "kafka-3:9092",
]

admin_client = KafkaAdminClient(bootstrap_servers=brokers, client_id='create_topics')

topic_list = []
topic_list.append(NewTopic(name="orders",    num_partitions=1, replication_factor=3))
topic_list.append(NewTopic(name="shipments", num_partitions=1, replication_factor=3))
topic_list.append(NewTopic(name="customers", num_partitions=1, replication_factor=3))

admin_client.create_topics(new_topics=topic_list, validate_only=False)
