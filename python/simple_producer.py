from distutils.command.config import config
from kafka import KafkaProducer
from datetime import datetime
import json
import uuid

def simple_producer(conf, topic_name, key, payload):
    producer = KafkaProducer(**conf)

    message = { 'tag' : 'simple_producer',
        'uuid' : str(uuid.uuid4()),
        'date' : datetime.now().isoformat(),
        'payload' : payload
    }
    
    print("Sending: {}".format(message))
    producer.send(topic_name, key=json.dumps(key).encode('utf-8'), value=json.dumps(message).encode('utf-8'))

    # Wait for all messages to be sent
    producer.flush()
