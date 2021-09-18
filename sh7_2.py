'''
در یک لیست از اسامی بدون استفاده از counter اعلام کند از هر اسم چند عدد وجود دارد
'''

names=['Ali', 'Reza', 'Iman','Ali', 'Mojtaba', 'Iman', 'Mojtaba', 'Ali','Mehrad',
 'Tara','Sahar','Shabnam','Sara','Hamid']

reapet = {}.fromkeys(names,0) 
 
for ch in names:
   if ch in reapet:
       reapet[ch] += 1

print(reapet)    
    
