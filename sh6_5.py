'''
در لیستی از اسامی مشخص کند اسم خواسته شده چندمین اسم لیست است 
'''

def namelist(lst, x, start=0, end= None):
    if end is None:
        end = len(lst) - 1
    if start > end:
        return False
    mid = (start + end) // 2
    if x == lst[mid]:
        return mid
    if x < lst[mid]:
        return namelist(lst, x, start, mid - 1)
    return namelist(lst, x, mid + 1, end)

a = ['Mehrad','Tara','Sahar','Shabnam','Sara','Hamid']

print(namelist(a, 'Sahar'))



