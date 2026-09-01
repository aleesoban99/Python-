num1 = int(input("Enter first number: "))
while True:
    op = input("Enter operation (+ - * /): ")
    num2 = int(input("Enter second number: "))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        print("Invalid operation")
        continue

    print(f"Answer is {result}")

    choice = input("Do you want another calculation with this answer? (y/n): ").lower()

    if choice == "n":
        break

    if choice == "y":
        num1 = result