student_name, student_age, student_is_registered = "Saleh", 24, True

print(type(student_age))
print(type(student_name))               #using type() so yk the data type
print(type(student_is_registered))

print(isinstance(student_age, int))            #using isinstance() for data type checking

age = input("Enter your age: ")                  #input is always STRING!

if isinstance(age, int):                    #If used لتنفيذ كود عند  تحقق الشرط
    print("You are", age + 5, "after 5 years")
else:
    print("You are", int(age) + 5, "after 5 years")

teacher_name = "Faisal"

print(teacher_name)

index = int(input("Select an index: "))

if index < len(teacher_name):                       #len used لعدد العناصر
    print(teacher_name[index])
else:
    print("Out of range")

print(type(len(teacher_name)))
