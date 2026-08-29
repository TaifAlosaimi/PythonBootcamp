students =["Sara", "Taif", "Mashael"]

for student in students:
    print(student)

iterable = enumerate(students)        #enumerate تعطي كل عنصر مع ال index الخاص فيه
print(next(iterable))                #next تعطيني العنصر التالي من ال enumerate
print(next(iterable))