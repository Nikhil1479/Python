def add(a, b):
    return a + b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a,b):
    return a/b

a = int(input("Enter first number: "))
op = input("Enter operation to perform: ")
b = int(input("Enter second number: "))

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

calculation_function = operations[op]
answer = calculation_function(a,b)

print(f"{a} {op} {b}: {answer}")