numbers = range(1,6)                     # start icluded, stop excluded so: 1,2,3,4,5

squares = {
    number : number ** 2                  # 1^2 , 2^2 , 3^2 , etc.....
    for number in numbers 
}


print(squares)