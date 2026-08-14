location = "Global"
def outter():
    location = "outter"
    print(f"From {location}")
    def inner():
        location = "inner"
        print(f"From {location}")
    inner()
outter()