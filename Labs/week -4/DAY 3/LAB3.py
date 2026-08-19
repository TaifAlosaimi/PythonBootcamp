class Welcome:
    def __init__(self, name):         #constructor يستقبل  name ويجهز ال attribute
        self.name = name                #attribute

    def welcome(self):                   #method تطبع رسالة
        print(f"Welcome {self.name}")




students = [                 #List تحتوي على objects
    Welcome("Taif"),
    Welcome("Dhai"),
    Welcome("Reef"),
]


for s in students:                  #for loop عشان امر على كل طالب
    s.welcome()                    #استدعيت ال welcome method لكل طالب