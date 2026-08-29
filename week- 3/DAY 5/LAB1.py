numbers = [1,2,3,4,5]                   #List of numbers
sqaured_numbers = []                         #عرفت متغير فاضي لأن رح أحتاجه                       

for number in numbers:
    sqaured_numbers.append(number ** 2)                    #ضيف لي على السكورد نمبر, نمبر أس 2

print(sqaured_numbers)




comp_numbers = [                     #نفس الشي لكن طريقة مختلفة , بالكمبرهنشن
    number ** 2                             #ُExpression
    for number in numbers                    #Close
]
print(comp_numbers)