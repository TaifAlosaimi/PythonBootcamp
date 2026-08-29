students = [
    {"name": "Taif", "scores": [99, 98,96]},
    {"name": "Mshael", "scores": [33, 38,49]}
]





report = [
    {"name": student["name"], 
     "average": f'{sum(student["scores"]) / len(student["scores"]):.2f}'
    }
    for student in students  
]




filitterd_report = [
    student
    for student in report
    if float(student["average"]) >= 60
]




index = {
    student["name"] : student
    for student in report
}




from copy import deepcopy
students_backup = deepcopy(index)

index["Taif"]["average"] = "99"

print(report)
print(filitterd_report)
print(index["Taif"])
print(students_backup["Taif"])