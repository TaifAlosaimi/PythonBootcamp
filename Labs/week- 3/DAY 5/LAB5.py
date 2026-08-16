nested_list = [[1,2], [3,4],[5,6]]
flattened_list = []
for row in nested_list:
    for column in row:
        flattened_list.append(column)
print(flattened_list)

comp_flattened_list = [
    column
    for row in nested_list
    for column in row
]
print(comp_flattened_list)