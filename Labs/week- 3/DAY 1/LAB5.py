def show_booking(destination, nights):
    print(f"You're traveling to {destination}, and stay for {nights} nights")

show_booking("Jeddah", 3)
show_booking("Doha", 5)


def show_booking(destination="Riyadh", nights=1):
    print(f"You're traveling to {destination}, and stay for {nights} nights")

show_booking("Jeddah", 3)
show_booking("Doha", 5)
show_booking("D", False)


def show_booking(destination="Riyadh", nights="1"):
    if nights.isdigit():
        nn = int(nights)
    print(f"You're traveling to {destination}, and stay for {nn} nights")

show_booking()
show_booking("Jeddah", "3")
show_booking("Doha", "5")