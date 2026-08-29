class Ticket:          #أنشأت كلاس اسمه ticket

    def __init__(self ,name , status = "Open"):         #constructor يجهزالاتربيوتس 
        self.name = name
        self.status = status         #attributes

    def newStatus(self, status):             #method
        self.status = status              #attribute


myTicket1 = Ticket("1000", "In-progress")       #instances
myTicket2 = Ticket("2000", "Pending")
print(myTicket1.status)
print(myTicket2.status)


