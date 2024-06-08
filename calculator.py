#Making Calculator In Python

num1 = int(input("Enter Number 1::="))
num2 = int(input("Enter Number 2::="))
opr = input("Enter Operator (+, -, *, /)::")

if opr == "+":
    print("Result is::", num1 + num2)
elif opr == "_":
    print("Result is::", num1 - num2)
elif opr == "*":
    print("Result is::", num1 * num2)
elif opr == "/":
    print("Result is::", num1 / num2)
else:
    print("Invalid Operator")





num3 = int(input("Enter Number 1::="))
num4 = int(input("Enter Number 2::="))
opr = input("Enter Operator (+, -, *, /)::")

if opr == "+":
    print("Result is::", num1 + num2)
if opr == "_":
    print("Result is::", num1 - num2)
if opr == "*":
    print("Result is::", num1 * num2)
if opr == "/":
    print("Result is::", num1 / num2)
if opr != "+" != "-" != "*" != "/":
    print("Invalid Operator")


