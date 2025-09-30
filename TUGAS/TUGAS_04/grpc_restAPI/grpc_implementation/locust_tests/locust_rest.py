from locust import HttpUser, task, between

class RestUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_data(self):
        with self.client.get("/get_data", params={"query": "Locust"}, catch_response=True) as resp:
            if resp.status_code != 200:
                resp.failure(f"Status {resp.status_code}: {resp.text}")
