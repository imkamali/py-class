'''
تابعی که دو عدد از ورودی بگیرد و بدون استفاده از علامت
 ضرب و توان اولی را به توان دومی برساند
'''

x=print(input('Enter x:'))
y=print(input('Enter y:'))

def pow_rec(x,y):
    if y == 0:
        return 1
    elif x == 0:
        return 0
    elif y == 1:
        return x
    else:
       def mul(x,y):
           if y == 0:
               return 0
           elif y == 1:
               return x
           else:
               return x + mul(x,y-1)
    print('mul=', mul(2,3))
                   
          
print('pow=',pow_rec(2,5))        
          
    
  

