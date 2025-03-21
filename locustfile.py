from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def get_home(self):
        self.client.get("/")

    @task(2)
    def post_data(self):
        self.client.post("/submit", json={"name": "John", "age": 30})

    @task(1)
    def trigger_error(self):
        self.client.get("/error")

