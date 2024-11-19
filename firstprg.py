# python calculator

operator = input("Enter the operator (+,-,/,*)? : ")
num1 = float(input("Enter the First Number: "))
num2 = float(input("Entre the Second Number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "/":
    result= num1 / num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
else:
    print(f" {operator} operator is not valid ")
