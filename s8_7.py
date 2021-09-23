'''
جذر با استفاده از اعداد
'''

import math
def SquareRoot(number):
    return math.log2(number )

numbers = [1,2,3,4]

sqr = list(map(SquareRoot,numbers))

print(sqr)