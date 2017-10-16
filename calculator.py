operation = raw_input("Choose math operation (+, -, *, /): ")

x = int(raw_input("Enter the value for X: "))
y = int(raw_input("Enter the value for Y: "))

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    raise ValueError("Wrong operation!")

