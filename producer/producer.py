import json
import requests
import time

from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic

TOPIC = "topic1"


def create_topic(topic):

    admin_client = KafkaAdminClient(
        bootstrap_servers="kafka:9092", 
        client_id='test'
    )

    topic_list = []
    topic_list.append(NewTopic(name=topic, num_partitions=1, replication_factor=1))
    try:
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
    except:
        print('Topic "{topic}" has already been created')


def producer(topic, cadence=2):

    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
    
    while True:
        api_req = requests.get("http://api:7777")

        if api_req.status_code != 200:
            print(f"Received status code {api_req.status_code}. Wait for 10")
            time.sleep(10)
        
        result = json.loads(api_req.text)

        pull_time, data_list = result['pull_time'], result['data']

        for data in data_list:
            producer.send(topic, value=bytes(str(data), 'utf-8'))
        
        time.sleep(cadence)


if __name__ == "__main__":
    time.sleep(10)
    create_topic(TOPIC)
    producer(TOPIC)
    