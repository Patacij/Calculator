x = int(raw_input("Vnesi zeljeno stevilo:" ) )
y = 3
z = 5

for i in range(x):
    if i % y == 0 and i % z == 0:
        print("Fizz Buzz")
    elif i % y == 0:
        print("Fizz")
    elif i % z == 0:
        print("Buzz")
    else:
        print(i)
