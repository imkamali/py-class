'''
کاراکتر n ام سری فیبوناچی را بدون استفاده از توابع بازگشتی چاپ کند
'''

a = 0
b = 1
n=int(input("Enter n: \n"))

while a < n-1:
       
    a  , b = b , a+b
    if False:
        break
print('The Nth character from the Fibonacci list:', b)