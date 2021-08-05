num1 = int(input ("Enter num1 please \n"))
num2 = int(input ("Enter num2 please \n"))
num3 = int(input ("Enter num3 please \n"))

if num1+num2 > num3 and num1 + num3 > num2 and num2+num3 > num1:
    print ("It's a triangle")
else:
    print ("It's not a triangle")
