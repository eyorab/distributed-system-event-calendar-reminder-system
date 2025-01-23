import pika

class UserProducer:
    def __init__(self, host='localhost', queue='user_queue'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.queue = queue
        self.channel.queue_declare(queue=self.queue)

    def publish_event(self, event):
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue,
                                   body=event)
        print(f" [x] Sent {event}")

    def close_connection(self):
        self.connection.close()

