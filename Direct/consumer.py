import pika
import time
import random

def on_message_recieved(channel, method, properties, body):
    time_to_process = random.randint(1, 6)
    channel.basic_ack(delivery_tag=method.delivery_tag)
    print(f'\nMessage {body} received. It will take process time {time_to_process} seconds.')
    time.sleep(time_to_process)
    print(f'\nMessage {body} processed!')

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.queue_declare(queue='messagebox')

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='messagebox', on_message_callback=on_message_recieved)

print('Start consumming')
channel.start_consuming()
