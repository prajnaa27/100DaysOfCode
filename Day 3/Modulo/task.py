#Check even or odd
from math import remainder

number=int(input("Enter a number: "))
remain=number%2
if remain:
    print(f"{number} is ODD")
else:
    print(f"{number} is even")