# A function is a  blok of code that perform a specifik task
# 1. Built in function
# 2. User defined function
# def functionName(argument)   function define
def calculeteGmen(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def isGreter(a,b):
    if(a>b):
        print("a is greter")
    else:
        print("b is greter")

a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
calculeteGmen(a,b)