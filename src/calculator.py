while True:
    number1 = input("enter the first number: ")
    operator = input("enter the operator: ")
    number2 = input("enter the second number: ")

    number1 = int(number1)
    number2 = int(number2)

    if operator == "+":
        print(number1 + number2)
    elif operator == "-":
        print(number1 - number2)
    elif operator == "*":
        print(number1 * number2)
    elif operator == "/":
        print(number1 / number2)
    elif operator == "%":
        print(number1 % number2)
    elif operator == "**":
        print(number1 ** number2)
    else:
        print("Incorrect Operator")
