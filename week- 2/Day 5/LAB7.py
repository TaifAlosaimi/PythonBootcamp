numbers = [4, 7, 10, 13, 16, 21, 22]
even_counter = 0

for num in numbers:
    if num % 2 == 0:
        even_counter += 1

print(f"Total even numbers is: {even_counter}")