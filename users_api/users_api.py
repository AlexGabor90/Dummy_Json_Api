"""
Creare clasa pentru interactionarea cu libraria 'requests'
url folosit = 'https://dummyjson.com/docs/users'
"""

import requests


class UsersApi:

    def get_all_users(self):
        get_user = requests.get("https://dummyjson.com/users")
        return get_user

    def get_user_by_id(self, user_id):
        get_user_id = requests.get(f"https://dummyjson.com/users/{user_id}")
        return get_user_id

    def search_user(self, user):
        search = requests.get("https://dummyjson.com/users/search", params={"q": user})
        return search

    def filter_users(self, key, value):
        payload = {"key": key, "value": value}
        filter_search = requests.get("https://dummyjson.com/users/filter", params=payload)
        return filter_search


    def limit_skip_users(self, limit, skip):
        payload = {'limit': limit, 'skip': skip,}
        limit = requests.get("https://dummyjson.com/users", params=payload)
        return limit

    def get_users_cart_by_user_id(self, user_id):
        user_cart = requests.get(f"https://dummyjson.com/users/{user_id}/carts")
        return user_cart

    def get_users_post_by_user_id(self, user_id):
        user_post = requests.get(f"https://dummyjson.com/users/{user_id}/posts")
        return user_post

    def get_users_todo_by_user_id(self, user_id):
        user_todo = requests.get(f"https://dummyjson.com/users/{user_id}/todos")
        return user_todo

    def add_new_user(self, add_user):
        new_user = requests.post("https://dummyjson.com/users/add", add_user)
        return new_user

    def update_user(self, user_id, update_info):
        update = requests.put(f"https://dummyjson.com/users/{user_id}", json=update_info)
        return update

    def delete_user(self, del_user):
        user_del = requests.delete(f"https://dummyjson.com/users/{del_user}")
        return user_del


user_object = UsersApi()


response1 = user_object.get_all_users()
print(response1)
print(response1.status_code)
print(response1.json())

print("--------------------------------------------------------------------")

response2 = user_object.get_user_by_id(1)
print(response2)
print(response2.status_code)
print(response2.json())

print("--------------------------------------------------------------------")

response3 = user_object.search_user("John")
print(response3)
print(response3.status_code)
print(response3.json())

print("--------------------------------------------------------------------")

response4 = user_object.filter_users("hair.color", "Blond")
print(response4.json())

print("--------------------------------------------------------------------")
response5 = user_object.limit_skip_users(5, 10)
print(response5.json())























