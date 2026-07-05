#A calculator for basic calculation
a = float(input("Enter first digit"))
b = float(input("enter second digit"))
operation = str(input("enter the operation +,-,*,/"))

def calculator(a,b,operation):
    match operation:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "/":
            if b == 0:
                return "Error: Division by zero"
            else:
                return a/b
        case _:
            return "Invalid operation"

print(calculator(a,b,operation))
