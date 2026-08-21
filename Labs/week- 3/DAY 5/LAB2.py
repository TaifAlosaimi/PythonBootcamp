prices = [10,25,40]              #List of prices

prices_with_vat = [                     #Comp 
    round(price * 1.15,2)               #Expression
    for price in prices                    #close
]

print(prices_with_vat)