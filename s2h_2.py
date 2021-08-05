##Is the first number divisible by the second or not?
fnum= int(input("Enter first number, please: \n"))
snum= int(input("Enter second number, please: \n"))

if fnum % snum == 0:
    print("The first number is divisible by the second")
else:
    print("The first number is not divisible by the second")
