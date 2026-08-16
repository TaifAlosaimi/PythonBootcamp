new_names = ["Mada", "Khadeja", "Yamam", "Mashael"]

upp = (
    name.upper()
    for name in new_names
)

print(list(upp))
print(next(upp))
print(next(upp))
print(list(upp))

print("-"*5)
for x in upp:
    print(x)

