c_temp = [20,33,15,1]             #List of integers

f_temp = [                         #Comprehension
    temp * 1.8 + 32               #Expression 
    for temp in c_temp              #Close
    if temp > 0                 #Filtering
]

print(f_temp)