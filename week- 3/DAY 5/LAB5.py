nested_list = [[1,2], [3,4],[5,6]]           #Nested list : ليست جوا ليست
flattened_list = []                     #ُEmpty list اخزن فيها اللي بسويه

for row in nested_list:                       #لكل عنصر في ال Nested list
    for column in row:                      #لكل عنصر في الليست الحالية اللي هي row
        flattened_list.append(column)             #بضيف الناتج على الامبتي لست
print(flattened_list)

 
comp_flattened_list = [                         #Comprehension, الطريقة الاسهل و نفس الاوتبت
    column                       #ُExpression
    for row in nested_list                      #Close
    for column in row                               #close
]
print(comp_flattened_list)