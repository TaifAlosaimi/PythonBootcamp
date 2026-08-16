list_name = ["Sara", "Dalal", "Taif","Nouf"]

counted_chars = [
    {"name":name, "count":len(name)}
    for name in list_name
]
print(counted_chars)