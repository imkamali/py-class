'''
یک لیست از اسامی موجود را بصورت تک کاراکتر در خطوط جدا چاپ کند.
'''
mylist =['Hanieh', 'Maryam', 'Mohammadreza', 'Rasa', 'saeed']

for name in mylist:
    lenght = len(name)
    i=0
    while i<lenght:
        print(name[i])
        i+=1
        
'''
 و یا اینکه یک لیست از اسامی از کاربر بگیرد و بصورت تک کاراکتر در خطوط جدا چاپ کند.
'''
mylist =[]
n=int(input("How many are on your list? \n"))

while len(mylist)<n:
    name = input("Enter your name: \n")
    mylist.append(name)
for name in mylist:
    lenght = len(name)
    i=0
    while i<lenght:
        print(name[i])
        i+=1
        



    