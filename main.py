#A calculator for basic calculation
a = int(input("Enter first digit"))
b = int(input("enter second digit"))
operation = str(input("enter the operation +,-,*,/"))

def cal(operation):
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

print(cal(operation))
