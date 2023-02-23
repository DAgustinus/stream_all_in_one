from kafka.admin import KafkaAdminClient, NewTopic
import time

time.sleep(10)


admin_client = KafkaAdminClient(
    bootstrap_servers="kafka:9092", 
    client_id='test'
)


topic_list = []
topic_list.append(NewTopic(name="topic1", num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)

"""
from kafka.admin import KafkaAdminClient, NewTopic
def check(s="INTERNAL://0.0.0.0:9092"):
    KafkaAdminClient(
        bootstrap_servers=s, 
        client_id='test'
    )
"""