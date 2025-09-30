from locust import HttpUser, task, between

class FileApiUser(HttpUser):
    wait_time = between(1, 3)  

    @task(1)
    def get_home(self):
        self.client.get("/")  
    @task(2)
    def get_small_file(self):
        self.client.get("/files/10kb.txt")

    @task(2)
    def get_medium_file(self):
        self.client.get("/files/100kb.txt")

    @task(2)
    def get_large_file(self):
        self.client.get("/files/1mb.txt")

    @task(1)
    def get_xlarge_file(self):
        self.client.get("/files/10mb.txt")
