listA = ['Hanieh', 'Maryam', 'Mohammadreza', 'Rasa', 'saeed','Roya']
listB =['Roya' , 'Raha', 'Hamid' , "Maryam",'Mehrad']

#listA.extend(listB)
setA=set(listA)
setB=set(listB)
print(setA.union(setB))
print(setA.intersection(setB))
print(len(setA.union(setB))-len(setA.intersection(setB)))