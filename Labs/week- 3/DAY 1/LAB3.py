print("Line One")
def gotofunc():
    print("From within the GoTo")

print("where is line 2?")
gotofunc()
print("i'm up here")

def unknowScope():
    print("Line one")
    def gotoFunc():
        print("From within the GoTo")                                #فنكشنز استدعيها بالطريقة اللي ابيها وعلى حسب وش ابغى output
    print("where is line 2?")
    gotofunc()
    print("i'm up here")
unknowScope()