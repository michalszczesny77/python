def restarting():

    while True:
        message = input("Type 'start' to enter new numbers or 'stop' to quit: ")

        if message.lower() == "start":
            break
        elif message.lower() == "stop":
            exit()
        else:
            print("Invalid input.")
            continue

def calculator():

    while True:
        try:
            operation_list = ['+', '-', '*', '/', '**']
            operation = input("Enter operation type: (+) (-) (*) (/) (**) ")

            if operation not in operation_list:
                print("Enter a correct character!")
                continue

            while True:
                try:
                    a = float(input("Enter first number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            while True:
                try:
                    b = float(input("Enter second number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            if operation == "+":
                output = a + b
            elif operation == "-":
                output = a - b
            elif operation == "*":
                output = a * b
            elif operation == "/":
                output = a / b
            elif operation == '**':
                output = a ** b

            print(f"Result: {round(output, 2)}")

            restarting()

        except ZeroDivisionError:
            print("You cannot divide by 0!")

            restarting()


calculator()