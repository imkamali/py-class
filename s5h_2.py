'''
لیستی از اعداد از کاربر بگیرد، به منفی که رسید متوقف شود
و در نهایت اعداد، جمع و میانگین آنها را چاپ کند
'''

numbers = list ()

while True:
    num=float(input("Enter number: \n"))
    if num < 0 :
        break
    numbers.append(num)
    listsum=sum(numbers)
    average=listsum/len(numbers)
    
print("For", numbers, "Sum is:", listsum, "and", "Average is:", round(average,2))

'''
راه حل دوم:
'''

numbers = list ()
listsum=0

while True:
    num=float(input("Enter number: \n"))
    if num < 0 :
        break
    else:
        numbers.append(num)
        listsum=listsum+num
        average=listsum/len(numbers)
    
print("For", numbers, "Sum is:", listsum, "and", "Average is:", round(average,2))