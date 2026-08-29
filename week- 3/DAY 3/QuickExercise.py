#

# colors = ["RED","YELLOW","ORANGE"]
# print(colors[0])
# print(colors[1])
# print(colors[-1])




# numbers = [10, 30,40,50]

# print(numbers[1:4])
# print(numbers[:3])
# print(numbers[::2])
# print(numbers[::-1])

# 'tasks = ["plan","code"]

# tasks[0] = "design"
# tasks.append("test")
# tasks.insert(1,"review")
# print(tasks)
# '


# scores = [90,39,55,54]

# scores.remove(39)
# last = scores.pop()
# scores.sort()

# print(scores)
# print(last)


# students = ["Taif", "Sara"]

# for student in students:
#     print(student)

# for index, student in enumerate(students):
#     print(index, student)

# for student in enumerate(students):
#     print(student)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# print(matrix[0])
# print(matrix[1][2])

# location = (24.666 , 99.39384)

# print(location[0])
# print(location[-1])


# student = ["Taif",22, "python",2026 ]

# name , age, course , *others = student

# print(name)
# print(age)
# print(course)
# print(others)

# skills = {"python", "Git", "python"}

# skills.add("Django")

# print(skills)
# print("Git" in skills)
# print(len(skills))






# backend = {"Python", "Django", "SQL"}
# frontend = {"HTML","CSS","Javascript","SQL"}

# print(backend | frontend)               #جيبهم كلهم بدون تكرار وبدون ترتيب حتى
# print(backend & frontend)            #هات الاشياء المتشابهه
# print(backend - frontend)                         #هات الاشياء الموجودة في باك اند وماهي موجودة في الفرونت اند




# students = {
#     "name" : "Taif",
#     "age" : 23,
#     "course" :"python"
# }



# student ={"name": "sara", "score": 90}
# student["score"] = 95
# student["grade"] = "A"

# email = student.get("email", "Not set")
# grade = student.pop("grade")

# print(student)
   




# student = {"name": "Sara", "score": 95}

# for key in student:
#     print(key)
# for value in student.values():
#     print(value)





# names = ["Sara", "Taif"]
# skills = {"Python", "Git"}
# student = {"name": "Sara", "score": 95}
# print(len(names))
# print("Python" in skills)
# print("score" in student)





# for student in students:
#         print(student["name"], student["score"])








# students = [
#     {
#         "name": "Sara",
#         "scores": (90, 85, 95), #tuble
#         "skills": {"Python", "Git"}  #set
#     },
#     {
#         "name": "Omar",
#         "scores": (80, 88, 92),
#         "skills": {"Python", "HTML"}
#     }
# ]

# for student in students:
#     total = 0
#     counter = 0

#     for score in student["scores"]:
#         total += score
#         counter += 1

#     average = total / counter

#     student["skills"].add("Django")

#     print(f"Name: {student['name']}")
#     print(f"Average: {average:.2f}")
#     print(f"Skills: {student['skills']}")
#     print()



