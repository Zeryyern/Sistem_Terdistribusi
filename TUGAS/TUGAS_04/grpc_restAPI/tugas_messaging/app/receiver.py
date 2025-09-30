import pika
import threading

SEND_QUEUE = "receiver_to_sender"
RECV_QUEUE = "sender_to_receiver"

def receive_messages(channel):
    def callback(ch, method, properties, body):
        print(f"\nSender: {body.decode()}\nYou: ", end="")
    channel.basic_consume(queue=RECV_QUEUE, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host="localhost",
            port=5672,
            credentials=pika.PlainCredentials("user", "password")
        )
    )
    send_channel = connection.channel()
    recv_channel = connection.channel()

    send_channel.queue_declare(queue=SEND_QUEUE, durable=True)
    recv_channel.queue_declare(queue=RECV_QUEUE, durable=True)

    threading.Thread(target=receive_messages, args=(recv_channel,), daemon=True).start()

    print("Type your messages (type 'exit' to quit):")
    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            break
        send_channel.basic_publish(exchange="", routing_key=SEND_QUEUE, body=msg)
        print(f"Sent: {msg}")

    connection.close()

if __name__ == "__main__":
    main()
