class Food:                    #أنشأت كلاس 
    def __init__(self, name):                  #Constructor 
        self.name = name                    #Attribute يخزن لي الاسم

    def ShowName(self):                  #method تعرض لي الاسم
        return self.name

class Fruites(Food):                 #سويت class يرث من الFood class
    def __init__(self , name, cal):
        super().__init__(name)                     #نستدعي الconstructor من ال parent class
        self.cal = cal                     #Attribute للكالوريز


    @staticmethod                #From method to staticmethod
    def stripname(newName):                  #method لها مهمة معينة
        return newName.strip()                      #مهمتها : حذف المسافات من بداية ونهاية ال string


myFav = Fruites("Apple", 70)                  #Object لل  child class 
print(myFav.ShowName())                            #طبعت الاوبجكت مع ميثود الشو نيم
print(myFav.stripname(  "TA            "))                          # طبعت الاوبجكت مع ميثود الستريب نيم
