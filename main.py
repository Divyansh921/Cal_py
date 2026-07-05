#A calculator for basic calculation

#defining a function for calculator

def calculator(a,b,operation):
    match operation:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "%":
            return "reminder is " + str(a%b)
        case "**":
            return "a raised to the power of b is " + str(a**b)
        case "//":
            if b == 0:
                return "Error: Division by zero"
            else:
                return "floor division is " + str(a//b)
        case "/":
            if b == 0:
                return "Error: Division by zero"
            else:
                return a/b
        case _:
            return "Invalid operation"


#while loop to keep the calculator running until user wants to exit
while True:
    print ("--New Calculation--")
    user = input("Do you want to continue? (y/n): ")
    if user.lower() == "n":
        print("Exiting the calculator")
        break
    elif user.lower() == "y":
        pass
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        continue
    a = float(input("Enter first digit: "))
    b = float(input("enter second digit: "))
    operation = str(input("enter the operation +,-,*,%,/,//,** "))
    print(calculator(a, b, operation))


