list_name = ["Sara", "Dalal", "Taif","Nouf"] 

counted_chars = [                      #List comprehension
    {"name":name, "count":len(name)}                 #Dictionary
    for name in list_name
]
print(counted_chars)