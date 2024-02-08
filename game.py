car_started = False
car_slowing_down = False

while True:
    command = input("> ").lower()
    if command == "start":
        if car_started:
            print("Car is already started")
        else:
            print("Car started")
            car_started = True
    elif command == "stop":
        if not car_started:
            print("Car is already stopped")
        elif car_slowing_down:
            print("The car is slowing down already")
        else:
            print("Car stopped")
            car_started = False
    elif command == "brake":
        if not car_started:
            print("Start the car first")
        elif car_slowing_down:
            print("The car is slowing down already")
        else:
            print("Car is slowing down")
            car_slowing_down = True
    elif command == "release brake":
        if not car_started:
            print("Start the car first")
        elif not car_slowing_down:
            print("The car is not slowing down")
        else:
            print("Car is not slowing down anymore")
            car_slowing_down = False
    elif command == "help":
        print("start - to start car \n stop - to stop car \n brake - to slow down car \n release brake - to release brake \n quit - to exit")
    elif command == "quit":
        print("Exiting the program.")
        break  # Exit the loop
    else:
        print("Sorry, I don't understand")
