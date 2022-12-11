from locust import HttpUser, task, between, TaskSet


class Basic(TaskSet):

    @task(1) #hello보내기
    def hello(self):
        self.client.post("hello")


    @task(1)   #index창받기
    def index(self):
        self.client.get("/index.html")

    @task(1)
    def contact(self):
        self.client.get("/")
        
    @task(3)
    def junk(self):
        self.client.get("/junk10MB.img")


    @task(3)
    def nothing(self):
        pass

class MyLocust(HttpUser):

    tasks = [Basic]
    min_wait = 5000
    max_wait = 10000