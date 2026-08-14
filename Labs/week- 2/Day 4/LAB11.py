command = input("Please enter a command").strip().lower()

match command:

    case "start":
        print("Starting system")

    case "stop":
        print("Stopping system")

    case "status":
        print("System is up and running ")

    case _:
        print("Please enter a proper command")