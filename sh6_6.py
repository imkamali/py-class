'''
جمله n ام سری فیبوناچی را با استفاده از توابع بازگشتی چاپ کند
'''
def fibo_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)

print('The 4th character from the Fibonacci list:',fibo_rec(4))   