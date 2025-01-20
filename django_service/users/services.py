import requests

class LaravelUserService:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_users(self):
        response = requests.get(f"{self.base_url}/api/users")
        return response.json()

    def create_user(self, data):
        response = requests.post(f"{self.base_url}/api/users", data=data)
        return response.json()

    def get_user(self, user_id):
        response = requests.get(f"{self.base_url}/api/users/{user_id}")
        return response.json()

    def update_user(self, user_id, data):
        response = requests.put(f"{self.base_url}/api/users/{user_id}", data=data)
        return response.json()

    def delete_user(self, user_id):
        response = requests.delete(f"{self.base_url}/api/users/{user_id}")
        return response.status_code == 204