def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator={'+':add ,'-':subtract,'*':multiply ,'/':divide}

def on_continue(n1):
    print("+\n-\n*\n/")
    operation = input("Pick an operation\n")
    num2 = int(input("What's the next number?\n"))
    calculate = calculator[operation]
    result = calculate(n1, n2)
    print(f"The result of {n1} {operation} {n2} = {result}")
    return result

#can store functions also in variables
to_continue='n'
while to_continue=='n':
    n1 = int(input("What's the first number?\n"))
    print("+\n-\n*\n/")
    operation = input("Pick an operation\n")
    n2 = int(input("What's the next number?\n"))
    calculate=calculator[operation]
    result=calculate(n1, n2)
    print(f"The result of {n1} {operation} {n2} = {result}")
    to_continue=input(f"Type 'y' to continue with {result} or type 'n' to start a new calculation\n").lower()
    while to_continue == 'y':
        result = on_continue(result)
        to_continue = input(f"Type 'y' to continue with {result} or type 'n' to start a new calculation\n").lower()
    print(result)