'''
ایجاد عدد رندوم بین یک تا صد بدون استفاده از متد randit
'''

from random import choice 

a = range(0,101)
mylist = list(a)


for i in range(101):
        x=choice(mylist)
        print(x)
        break      
    