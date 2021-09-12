# Car Game
command = ""
started = False
stopped = False

while True:
    command = input("Type 'help for commands' > ").lower()
    if command == 'start':
        if started:
            print("Car has already started.")
        else:
            started = True
            print("Car started...")

    elif command == "stop":
        if not started:
            print("Car has already stopped.")
        else:
            started = False
            print("Car stopped...")

    elif command == 'help':
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quite
        """)
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand that.")