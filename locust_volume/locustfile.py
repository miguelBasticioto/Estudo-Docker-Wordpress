from locust import HttpLocust, TaskSet

def login(l):
    l.client.post("/login", {"username":"miguel", "password":"123456"})

def logout(l):
    l.client.post("/logout", {"username":"miguel", "password":"123456"})

def index(l):
    l.client.get("/2019/03/22/imagem-1mb/")

#/2019/03/22/imagem-1mb/
#/2019/03/22/imagem-400kb-e-texto/
#/2019/03/22/imagem-300kb-e-20kb-de-texto/

class UserBehavior(TaskSet):
    tasks = {index: 2}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000