from audioop import mul


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

def operation():
    return input("Select operation: ")

def banner():
    print("======================")
    print("SHELL-CALCULATOR...")
    oparations=['+ Add','- Reduce','* Multiply','/ Devide','$ Exit']
    for i in oparations:
        print(i)
    print("======================")

def printAns(data,opp):
    if(opp=='+'):
        ans=add(data[0],data[1])
    elif(opp=='-'):
        ans=reduce(data[0],data[1])
    elif(opp='*'):
        ans=multiply(data[0],data[1])
    elif(opp=='/'):
        ans=devide(data[0],data[1])
    print("{0} {1} {2} = {3}".format(data[0],opp,data[1],ans))

while 1:
    banner()
    o=operation()
    if(o=='$'):
        print(".!.!................!.!.")
    data=getData()
    printAns(data,o)
