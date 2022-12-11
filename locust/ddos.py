# locustfile.py
from locust import HttpUser, task, between, TaskSet
import string

class Ddos(TaskSet):

    @task(1)
    def index(l):
        resp = l.client.get("/")
        print(resp.headers)


class LocustUser(HttpUser):
    tasks = [Ddos]
    min_wait = 100
    max_wait = 500
