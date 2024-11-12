import pika
import time
import random

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.queue_declare(queue='messagebox')

id = 1

while True:
    message = f'Message {id}'
    channel.basic_publish(exchange='', routing_key='messagebox', body=message)
    time.sleep(random.randint(1, 4))
    print(f'Message {message} sent successfully')
    time.sleep(2)
    id += 1
