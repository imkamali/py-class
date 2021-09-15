'''
یک fullname از کاربر بگیرد و اسم و فامیل را در دو خط جداگانه چاپ کند.
'''

fullname =input('Enter your fullname: \n')

       
for ch in fullname:
    
        if ch==' ':
            print()
            continue
        
        else:
            print(ch,end='')


        