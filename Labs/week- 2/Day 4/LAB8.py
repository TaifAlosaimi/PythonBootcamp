age_text = input("Enter your age").strip()

if age_text.isdigit():
    age = int(age_text)
    print(f"You will be {age + 5} in 5 years")

else:
    print("Enter a number")