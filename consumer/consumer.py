import time

from kafka import KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic


TOPIC = "topic1"


def consumer(topic, cadence=2):

    consumer = KafkaConsumer(topic,
                        #  group_id='my-group',
                         bootstrap_servers=['kafka:9092'])
    while True:
        for message in consumer:
            # message value and key are raw bytes -- decode if necessary!
            # e.g., for unicode: `message.value.decode('utf-8')`
            print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                message.offset, message.key,
                                                message.value))
            
        time.sleep(cadence)


if __name__ == "__main__":
    time.sleep(10)
    consumer(TOPIC)
