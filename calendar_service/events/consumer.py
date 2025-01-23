import json
import pika

class Consumer:
    def __init__(self, queue_name='user_queue', host='localhost'):
        self.queue_name = queue_name
        self.host = host
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)
        self.message = None 
    def callback(self, ch, method, properties, body):
        print(f" [x] Received {body}")
        self.message = json.loads(body)
        print(self.message)
    
    def start_consuming(self):
        self.channel.basic_consume(queue=self.queue_name,
                                   on_message_callback=self.callback,
                                   auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

if __name__ == "__main__":
    consumer = Consumer()
    consumer.start_consuming()
