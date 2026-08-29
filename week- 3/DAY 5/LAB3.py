names = ["AReEj" , "SaRa", "nasser", "Taif"]             #List of names 
lower = [name.lower() for name in names ]          #lower أحرف
upper = [name.upper() for name in names ]           #Upper أحرف                #Three comprehensions
titled = [name.title() for name in names ]            #Caps first letter

print(titled,upper,lower)