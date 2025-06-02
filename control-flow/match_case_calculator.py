num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print (f"The result is: {num1 + num2}")
    case "-":
        print (f"The result is: {num1 - num2}")
    case "*":
        print (f"The result is: {num1 * num2}")
    case "/":
        if num2 == 0:
            print ("Error: Division by zero.")
        else:
            print (f"The result is: {num1 / num2}")
    case _:
        print ("Invalid operation.")