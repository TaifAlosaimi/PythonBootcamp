location = "Global"          #Global variable


def outter():           
    location = "outter"       #Local variable تبع دالة outter
    print(f"From {location}")
    def inner():
        location = "inner"                #Local variable تبع دالة inner
        print(f"From {location}")
    inner()
outter()