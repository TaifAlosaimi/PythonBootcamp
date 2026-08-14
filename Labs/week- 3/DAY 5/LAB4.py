c_temp = [20,33,15,1]

f_temp = [
    (temp * 1.8 + 32)
    for temp in c_temp
    if temp > 0
]

print(f_temp)