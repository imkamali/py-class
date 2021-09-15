'''
لیستی از اعداد بدون استفاده از متد sort مرتب شود
'''

A= [1, 9, 8, 2, 10, 17, 55, 89, 19, 20]

def listsort(A): 

    for i in range(len(A)): 
          
        min_idx = i 
        for j in range(i + 1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j                   
        A[i], A[min_idx] = A[min_idx], A[i] 
    return A

print('list A:', A)
print('sorted list A:', listsort(A))        
        
        
        
        
    