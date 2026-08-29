prices = [25 , 30 ,55, 115]
total = 0

for price in prices:
    total += price

print(f"your total is = {total} ,VAT = {total * (15 / 100)} ")