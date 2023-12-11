"""
Creare clasa pentru interactionarea cu libraria 'requests'
url folosit = 'https://dummyjson.com/docs/products'
"""

import requests


class ProductsApi:

    def get_all_products(self):
        get_all_prod = requests.get("https://dummyjson.com/products")
        return get_all_prod

    def get_products_by_id(self, prod_id):
        get_prod = requests.get(f"https://dummyjson.com/products/{prod_id}")
        return get_prod

    def search_products(self, search_criteria):
        search_prod = requests.get(url="https://dummyjson.com/products/search", params={"q": search_criteria})
        return search_prod

    def get_products_categories(self):
        get_all_prod_category = requests.get(url="https://dummyjson.com/products/categories")
        return get_all_prod_category

    def get_products_of_category(self, prod_category_items):
        get_prod_category_item = requests.get(f"https://dummyjson.com/products/category/{prod_category_items}")
        return get_prod_category_item

    def add_product(self, add_prod):
        add_new_prod = requests.post(f"https://dummyjson.com/products/add", add_prod)
        return add_new_prod

    def update_product(self, id_prod, update_prod):
        updated_product = requests.put(f"https://dummyjson.com/products/{id_prod}", json=update_prod)
        return updated_product

    def delete_product(self, deletion_id):
        delete_prod = requests.delete(f"https://dummyjson.com/products/{deletion_id}")
        return delete_prod


product_obj = ProductsApi()

response1 = product_obj.get_all_products()
print(response1)
print(response1.status_code)
print(response1.json())

print("--------------------------------------------------------------------")

response2 = product_obj.get_products_by_id(1)
print(response2)
print(response2.status_code)
print(response2.json())
response_search_field = response2.json()
print(response_search_field['title'])

print("--------------------------------------------------------------------")

response3 = product_obj.search_products("phone")
print(response3)
print(response3.status_code)
response_msg = response3.json()
print(response_msg)
print(len(response_msg))

print("--------------------------------------------------------------------")

response4 = product_obj.get_products_categories()
print(response4)
print(response4.status_code)
print(response4.json())

print("--------------------------------------------------------------------")

response5 = product_obj.get_products_of_category("laptops")
print(response5)
print(response5.status_code)
response_category_msg = response5.json()
print(response_category_msg)
print(len(response_category_msg))

print("--------------------------------------------------------------------")

produs_nou = {
    "title": "BEMWEU",
    "price": 321421421,
    "description": "merge tare",
}
response6 = product_obj.add_product(produs_nou)
print(response6)
print(response6.status_code)
response_new_prod = response6.json()
print(response_new_prod)

print("--------------------------------------------------------------------")

response7_extra = product_obj.get_products_by_id(1)
print(response7_extra.json())

response7_update = {
    "title": "titlu schimbat",
    "description": "nimic",
    "price": "gratis",
}
response7 = product_obj.update_product(1, response7_update)
print(response7.json())

print("--------------------------------------------------------------------")

response8_extra = product_obj.get_products_by_id(100)
print(response8_extra.json())
response8 = product_obj.delete_product(100)
print(response8.json())
print(f"Is deleted? --{response8.json()['isDeleted']}--, on which date? --{response8.json()['deletedOn']}--")

