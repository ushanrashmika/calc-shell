def add(a,b):
    return a+b

def reduce(a,b):
    return a-b

def multiply(a,b):
    return a*b

def devide(a,b):
    return a/b

def getData():
    return [int(input("Enter first number: ")),int(input("Enter second number: "))]

def operation(o):
    return input("Select operation: ")

def banner():
    print("SHELL-CALCULATOR...")

while 1:
    banner()
