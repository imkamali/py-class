print("-----------Animals--------------------")

class Animals():
    def __init__(self, kind, age):
        
        self.kind = kind
        self.age = age
        
pet = Animals("dog", 3)

print("kind:", pet.kind,"///age:", pet.age)
print("------------------------------------\n")

print("-----------------Cars---------------")

class Cars():
    def __init__(self, brand, model, cylinders ):
        
        self.brand = brand
        self.model = model
        self.cylinders = cylinders
        
mycar = Cars("Renault", 2016, 4)

print("brand:", mycar.brand,"///model:", mycar.model, "///cylinders:", mycar.cylinders)
print("------------------------------------\n")

print("-----------------Flowers---------------")

class Flowers():
    def __init__(self, name, kind, colour ):
        
        self.name = name
        self.kind = kind
        self.colour = colour
        
flower = Flowers("Rose", "Shrub", "Red")

print("name:", flower.name,"///kind:", flower.kind, "///colour:", flower.colour)
print("------------------------------------\n")

print("-----------------Field of Study---------------")

class Field():
    def __init__(self, title, degree, major ):
        
        self.title = title
        self.degree = degree
        self.major = major
        
StudyField = Field("Civil", "Master", "Seismic")

print("title:", StudyField.title,"///degree:", StudyField.degree, "///major:", StudyField.major)
print("------------------------------------\n")

print("-----------------Countries---------------")

class Countries():
    def __init__(self, Name, Area, Population ):
        
        self.Name = Name
        self.Area = Area
        self.Population = Population
        
country = Countries("Iran", "1648000 km^3", 83000000)

print("Name:", country.Name,"///Area:", country.Area, "///Population:", country.Population)
print("------------------------------------\n")

