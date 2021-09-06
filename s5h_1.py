'''
دو عدد از کاربر می گیرد از عدد بزرگ تا عددکوچک شمارش را چاپ می کند.
'''
x= int(input("enter x: \n"))
y= int(input("enter y: \n"))

if x<y:
    while x<=y:
        print(y)
        y-=1
elif x>y:
    while x>=y:
        print(x)
        x-=1
    
