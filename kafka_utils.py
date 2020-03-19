from kafka import KafkaProducer, KafkaConsumer

_BOOTSTRAP_SERVER = ['localhost:9092']


def connect_kafka_producer():
    """    
    Create Kafka Producer
    """
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=_BOOTSTRAP_SERVER)
    except Exception as ex:
        print("Error in creating Producer -> ",str(ex))
    finally:
        return _producer


def connect_kafka_consumer(topic):
    """    
    Create Kafka Consumer
    """
    _consumer = None
    try:
        _consumer = KafkaConsumer(topic,
                                  bootstrap_servers=_BOOTSTRAP_SERVER,
                                  auto_offset_reset='earliest',
                                  consumer_timeout_ms=100
                                  )
    except Exception as ex:
        print("Error in creating Consumer -> ", str(ex))
    finally:
        return _consumer



def publish_message(producer, topic_name, key, value):
    """    
    Hashed Message logging for a producer
    Ensures all messages sent to the same partition
    """
    try:
        key_bytes = bytes(key, 'utf-8')
        value_bytes = bytes(value, 'utf-8')
        # Publish a Message to the given topic
        producer.send(topic_name, key=key_bytes, value=value_bytes)
        # Makes all buffered records immediately available
        producer.flush()
        print("Message published successfully!")
    except Exception as ex:
        print("Exception is --> ", str(ex))
