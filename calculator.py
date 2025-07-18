print("Welcome to the simple calculator!")
print("Available operations: +,-,*,/")
num1=float(input("Enter a number:"))
num2=float(input("Enter another number:"))
operation=input("Enter operation:")
if(operation== '+'):
    result=num1+num2
    print(f"{num1} + {num2} =",result)
elif(operation=='-'):
    result=num1-num2
    print(f"{num1} - {num2} =",result)
elif(operation== '*'):
    result=num1*num2
    print(f"{num1} * {num2} =",result)
elif(operation=='/'):
    result=num1/num2
    print(f"{num1} / {num2} =",result)
else:
    print("invalid input")
    