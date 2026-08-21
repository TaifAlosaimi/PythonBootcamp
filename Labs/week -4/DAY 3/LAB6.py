class Food:                    #أنشأت كلاس 
    def __init__(self, name):                  #Constructor 
        self.name = name                    #Attribute يخزن لي الاسم

    def ShowName(self):
        return self.name

class Fruites(Food):                 #سويت class يرث من الFood class
    def __init__(self , name, cal):
        super().__init__(name)                     #نستدعي الconstructor من ال parent class
        self.cal = cal                     #Attribute للكالوريز


    @staticmethod                #From method to staticmethod
    def stripname(newName):
        return newName.strip()


myFav = Fruites("Apple", 70)
print(myFav.ShowName())
print(myFav.stripname(  "TA            "))
