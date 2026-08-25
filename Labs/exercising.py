products = [
    {"name": "Laptop", "price": 4500, "tags": ["tech", "work"], "stock": 5},
    {"name": "Mouse", "price": 120, "tags": ["tech"], "stock": 0},
    {"name": "Notebook", "price": 25, "tags": ["study", "office"], "stock": 20},
    {"name": "Headphones", "price": 350, "tags": ["tech", "music"], "stock": 8},
]
#دكشنري عادي فيه بيانات


available_products = [
    product["name"]
    for product in products
    if (product["stock"]) > 0
]
#كمبرهنشن 


expensive_products = [
    product["name"]
    for product in products
    if product["price"] > 300
]
#كمبرهنشن فيه فيلترنق



tags = [
    tag
    for product in products
    for tag in product["tags"]
]
#كمبرهنشن


uniqe_tags = {
    tag
    for tag in tags
}
#برضو كمبهنشن


price_index = [
    {"name" : product["name"] , "price" : product["price"]}
     for product in products
]

#كمبرهنشن جواها دكشنري


backup = products
#مافهمت كثير وش الباك اب وليه سويناه
backup[0]["name"] = "taioofa"

print(backup)
print(price_index[0])
print(uniqe_tags)
print(tags)
print(available_products)
print(f' expensive_products : {expensive_products}')
