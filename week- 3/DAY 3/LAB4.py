tasks = ["Read email","Open ticket"]

tasks[0] = "Login"          #استبدله بالعنصر الموجود في index 0
tasks.append("Get coffee")
tasks.insert(0, "Get breakfast")               #اضيف عنصر في index 0
tasks.pop(3)                #delete
print(tasks)
