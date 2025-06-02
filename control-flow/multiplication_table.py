number = int(input("Enter a number to see its multiplication table:"))
x = number
for y in range(1,11):
    z = x * y
    print(x, "*", y, "=", z)
