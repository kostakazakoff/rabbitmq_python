import pika
from pika.exchange_type import ExchangeType

def on_message_recieved(channel, method, properties, body):
    print(f'First consumer recieved message: {body}')

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(queue=queue.method.queue, exchange='pubsub')

channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_recieved)

print('Start consumming')
channel.start_consuming()
