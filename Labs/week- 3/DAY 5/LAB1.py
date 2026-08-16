numbers = [1,2,3,4,5]
sqaured_numbers = []

for number in numbers:
    sqaured_numbers.append(number ** 2)

print(sqaured_numbers)




comp_numbers = [
    number ** 2 
    for number in numbers
]
print(comp_numbers)