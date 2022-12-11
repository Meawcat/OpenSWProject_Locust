# locustfile.py
from locust import HttpUser, task, between, TaskSet
import string
import random

def passwd(): #자리수 6~10의 랜덤 패스워드 생성
    n = random.randint(6,10)
    rand_str = ""
    for i in range(n):
        rand_str += str(random.choice(string.ascii_letters+ string.digits))
    return rand_str

class post_pwd(TaskSet):

    @task(2)
    def index(l):
        l.client.get("/")

    @task
    def login_post(l):
        pwd = passwd()
        l.client.post("",json = {"password": pwd})
        #if resp.login == "success":
            #print("passwd = " + passwd)



class LocustUser(HttpUser):
    tasks = [post_pwd]
    min_wait = 1000
    max_wait = 5000

    