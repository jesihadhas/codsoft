print("CALCULATOR")

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

print("press 1 for addition")
print("press 2 for substraction")
print("press 3 for multiplication")
print("press 4 for division")

operator=int(input("Enter the arithmetic operator:"))

if operator==1:
    print(("Answer="),num1+num2)
elif operator==2:
    print(("Answer="),num1-num2)
elif operator==3:
    print(("Answer="),num1*num2)
elif operator==4:
    print(("Answer="),num1/num2)
else:
    print("invalid input")
        