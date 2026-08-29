message = ("please enter your age ?")
age_text = input(message)

while not age_text.isdigit():
    age_text = input(message).strip() 

age = int(age_text)
print(f"you are :{age}")