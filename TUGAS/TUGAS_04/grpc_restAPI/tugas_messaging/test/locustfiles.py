from locust import User, task, between
import subprocess

class MessagingUser(User):
    wait_time = between(1, 3)

    @task
    def send_message(self):
        # Simulate sender sending a message
        subprocess.run(["python", "app/sender.py"], capture_output=True)

    @task
    def receive_message(self):
        # Simulate receiver sending a message (bi-directional)
        subprocess.run(["python", "app/receiver.py"], capture_output=True)
