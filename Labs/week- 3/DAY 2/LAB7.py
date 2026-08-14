rate = 0.15
def getTotal(amount):
    total = amount * rate + amount
    return total
print(f"{getTotal(199.99):.2f}")
print(round(getTotal(199.99)))
print(round(getTotal(199.99), 2))

