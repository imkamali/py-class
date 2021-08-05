num1 = float (input("Enter num1 : \n"))
num2 = float (input("Enter num2 : \n"))
num3 = input ("operation :\n")
sum = num1 + num2
less =num1 - num2
if num3 == 'sum' :
    print ('sum=' , sum)
elif num3 == 'less':
    print ('less=', less)
else:
    prin ("I don't know")
