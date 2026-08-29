class Greeter:                      #انشأت كلاس
    def __init__(self, message):                  #جهزته وحطيت الباراميترز 
        self.message = message               #attribute is done

    def greet(self, user):                    #Method
        self.user = user                     #attribute
        return(f"Hello {user}, {self.message}")


mygreet = Greeter("Welcome to Tuwaiq")          #أنشأت اوبجكت اسمه mygreet
mymsg = mygreet.greet("Taif")                    #هنا رح تتخزن لي القيمة اللي رجعتها method greet
print(mymsg)