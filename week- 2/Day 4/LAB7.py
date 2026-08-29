name = input("please enter your first name").strip()

if not name:
    print("please enter a name")
elif not name.replace(" ","").isalpha():
    print("name must contain letters")
else:
    print(f"vaild name {name}")