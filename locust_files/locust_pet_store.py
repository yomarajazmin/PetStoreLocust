import time, json, random
from locust import HttpUser, task, between

class APITestUser(HttpUser):
    wait_time = between(1, 2)  

    @task
    def get_pet_by_status(self):
        self.client.get("/pet/findByStatus?status=pending")
        
    @task
    def get_pet_by_tag(self):
        self.client.get("/pet/findByTags?tags=tag101")
        
    @task
    def get_pet_by_id(self):
        self.client.get("/pet/10")

    @task
    def get_store_invetory(self):
        self.client.get("/store/inventory")

    @task
    def get_order_by_id(self):
        self.client.get("/store/order/107")

    @task
    def user_login(self):
        self.client.get("/user/login?username=theUser101&password=12345")
