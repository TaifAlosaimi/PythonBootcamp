prices = [10,25,40]

prices_with_vat = [
    round(price * 1.15,2)
    for price in prices
]

print(prices_with_vat)