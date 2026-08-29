location = 0
def outter():
    location = 1
    print(f"From {location}")
    def inner():
        location = 2
        print(f"From {location}")
    inner()
outter()