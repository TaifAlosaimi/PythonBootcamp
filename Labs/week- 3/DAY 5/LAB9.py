new_names = ["Mada", "Khadeja", "Yamam", "Mashael"]

upp = (                  #Generator Expression 
    name.upper()
    for name in new_names
)

print(next(upp))                 #ناخذ القيمة التالية من الجنريتر ونطبعها
print(next(upp))
print(list(upp))                         #ناخذ القيم الباقية من الليست كلها ونطبعها

print("-"*5)                          #فاصل بس

for x in upp:                    #الطريقة البيسك
    print(x)
