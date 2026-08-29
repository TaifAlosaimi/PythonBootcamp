#Name-Mangling
#Property

class Student:                            #I created a class called"student"
    __enrolled = True                          #Private attribute لتخزين حالة التسجيل الافتراضية
    def __init__ (self,name, enrolled):            #Constructar يشتغل اذا شغلنا اوبجكت
        self.name = name                    # attribute 
        self.score = []                       #Empty list لتخزين درجة الطالب



    def add_score(self,score):                 #Method لإدخال درجة الطالب          
        if 0 < score > 100:
            raise ValueError("Score must be between 0 and 100")      #إذا الدرجة مب صحيحة يظهر Error
        self.score.append(score)


    #Getter
    @property                                               #نخلي enrolled تعمل ك بروبرتي بدل مانستدعيها ك method
    def enrolled(self):                             #Getter تقرا قيمة enrolled
        return self._enrolled               #رجعنا قيمة الprivate attribute

    #Setter
    @enrolled.setter                     #setter لتغيير قيمة enrolled
    def enrolled(self, status):                     #يستقبل القيمة الجديدة للحالة
        self._enrolled = status                         #تحديث قيمة enrolled


    @property                       #نخلي average تعمل ك property
    def average(self):                  
        if not self.score:                     #إذا ليست الدرجات فاضية..
            return 0                                  #نرجع صفر
        else:
            return sum(self.score)/len(self.score)             #إذا لا؟ نسوي افرج


student = Student("Taif", None)
student.add_score(80)
student.add_score(90)
student.add_score(100)
print(student.average)
student.enrolled = True                    #SETTER لتغيير حالة التسجيل
student.enrolled = False
print(student.enrolled)
print(student.score)
print(student.name)