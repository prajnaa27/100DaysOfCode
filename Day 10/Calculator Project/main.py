import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculate(n1,n2,operation):
    if operation=='+':
        return add(n1,n2)
    elif operation=='-':
        return subtract(n1,n2)
    elif operation=='*':
        return multiply(n1,n2)
    elif operation=='/':
        return n1/n2
    else:
        print("Invalid operation\n")
        return None

def on_continue(n1):
    print("+\n-\n*\n/")
    operation = input("Pick an operation\n")
    n2 = int(input("What's the next number?\n"))
    result = calculate(n1, n2, operation)
    print(f"The result of {n1} {operation} {n2} = {result}")
    return result

choice='n'
while choice=='n':
        n1=int(input("What's the first number?\n"))
        print("+\n-\n*\n/")
        operation=input("Pick an operation\n")
        n2=int(input("What's the next number?\n"))
        result=calculate(n1,n2,operation)
        print(f"The result of {n1} {operation} {n2} = {result}")
        isContinue=input(f"Type 'y' to continue with {result} or type 'n' to start a new calculation\n").lower()
        while isContinue=='y':
            result=on_continue(result)
            isContinue=input(f"Type 'y' to continue with {result} or type 'n' to start a new calculation\n").lower()

        # print(f"Choice is {inner_choice}")







