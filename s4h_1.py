#دو کلاس A , B داریم،
#1-اجتماع دو کلاس
#2-اشتراک دوکلاس
#3-تعداد کسانی که فقط در یکی از کلاسها هستند
#4-اسامی کسانی که فقط در یکی از کلاسها هستند 

listA = ['Hanieh', 'Maryam', 'Mohammadreza', 'Rasa', 'saeed','Roya']
listB =['Roya' , 'Raha', 'Hamid' , "Maryam",'Mehrad']

setA=set(listA)
setB=set(listB)
print("A∪B=", setA.union(setB))
print("A∩B=", setA.intersection(setB))
print("The number of (A∪B)-(A∩B)=", len(setA.union(setB))-len(setA.intersection(setB)))
print("Members of (A∪B)-(A∩B)=", setA.union(setB)-(setA.intersection(setB)))