name = "Taif"

try:
    name = "A"
except TypeError as e:
    print(e)

x = 5
y = 5

if (x is y):
    print("They are the same value")
else:
    print("They are not the same value")

x += 5

print(y)
print(x)
print(id(x))
print(id(y))