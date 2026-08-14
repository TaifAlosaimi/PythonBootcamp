products = [
    {"name": "Laptop", "price": 4500, "tags": ["tech", "work"], "stock": 5},
    {"name": "Mouse", "price": 120, "tags": ["tech"], "stock": 0},
    {"name": "Notebook", "price": 25, "tags": ["study", "office"], "stock": 20},
    {"name": "Headphones", "price": 350, "tags": ["tech", "music"], "stock": 8},
]

available_products = [
    product["name"]
    for product in products
    if (product["stock"]) > 0
]


expensive_products = [
    product["name"]
    for product in products
    if product["price"] > 300
]



tags = [
    tag
    for product in products
    for tag in product["tags"]
]

print(tags)
print(available_products)
print(f' expensive_products : {expensive_products}')
