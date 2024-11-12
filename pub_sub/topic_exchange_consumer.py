import pika
from pika.exchange_type import ExchangeType

def on_message_recieved(channel, method, properties, body):
    print(body)

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

exchange_name = 'topic_exchange'
routing_key = '*.new.*'

channel.exchange_declare(exchange=exchange_name, exchange_type=ExchangeType.topic)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(queue=queue.method.queue, exchange=exchange_name, routing_key=routing_key)

channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_recieved)

print('Start consumming')
channel.start_consuming()
