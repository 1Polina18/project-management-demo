# calculator/calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == '+':
        result = add(x, y)
    elif op == '-':
        result = subtract(x, y)
    elif op == '*':
        result = multiply(x, y)
    elif op == '/':
        result = divide(x, y)
    else:
        print("Invalid operation!")
        exit(1)

    print(f"The result is: {result}")