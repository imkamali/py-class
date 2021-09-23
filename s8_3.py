
import sqlite3

fname= ['Ali', 'Mahdi','Shamim', 'Hanieh']
lname= ['Kabiri', 'Rezaee', 'Omidi', 'Hosseini']
age= [18, 25, 46, 73]
classmate= ['A', 'B', 'C', 'D']
point= [12, 18, 20,15]

conn = sqlite3.connect('D:\Training 1400\pyclass\session7\learn.db')

for fname, lname, age, classmate, point in zip(fname, lname, age, classmate, point):


    query =  f"insert into students2 values ('{fname}', '{lname}', {age}, '{classmate}', {point})"


    cursor = conn.cursor()

    cursor.execute(query)
    
    
    

conn.commit()




