student_name, student_age, student_is_registered = "Saleh2", 24, True

print(type(student_age))
print(type(student_name))
print(type(student_is_registered))

print(isinstance(student_age, int))

age = input("Enter your age: ")

if isinstance(age, int):
    print("You are", age + 5, "after 5 years")
else:
    print("You are", int(age) + 5, "after 5 years")

teacher_name = "Faisal"

print(teacher_name)

index = int(input("Select an index: "))

if index < len(teacher_name):
    print(teacher_name[index])
else:
    print("Out of range")

print(type(len(teacher_name)))
