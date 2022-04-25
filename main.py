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
    while 1:
        d0=input("Enter first number: ")
        try:
            d0=int(d0)
            break
        except:
            print("Invalid character. [Enter only numbers]")
            continue
    while 1:
        d1=input("Enter second number: ")
        try:
            d1=int(d1)
            break
        except:
            print("Invalid character. [Enter only numbers]")
            continue
    return [d0,d1]

def operation():
    return input("Select operation: ")

def banner():
    print("="*22)
    print("SHELL-CALCULATOR...")
    oparations=['+ Add','- Reduce','* Multiply','/ Devide','$ Exit']
    for i in oparations:
        print(i)
    print("="*22)

def printAns(data,opp):
    if(opp=='+'):
        ans=add(data[0],data[1])
    elif(opp=='-'):
        ans=reduce(data[0],data[1])
    elif(opp=='*'):
        ans=multiply(data[0],data[1])
    elif(opp=='/'):
        ans=devide(data[0],data[1])
    print("    {0} {1} {2} = {3}".format(data[0],opp,data[1],ans))

while 1:
    banner()
    o=operation()
    if(o in ['+','-','*','/','$']):
        if(o=='$'):
            print(".!.!........EXIT........!.!.")
            exit()
    else:
        print("Invalid Operation!.!.!")
        continue
    data=getData()
    printAns(data,o)
    input("=>> Press Any Key To Next Calculation")
    print("_"*22)
