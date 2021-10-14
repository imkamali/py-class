class Adam:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def salam(self):
        print(f'salam man {self.name} hastam {self.age}sale az TEH')
        
# class Daneshjoo:
#     def __init__(self, name, age, major):
#         self.name = name
#         self.age = age
#         self.major = major
#     def salam(self):
#         print(f'salam man {self.name} hastam {self.age}, {self.major}')

class Karmand(Adam):
    def __init__(self, name, age, job, office):
        Adam.__init__(self,name, age)
        self.job = job
        self.office = office
    # override
    def salam(self):
        print(f'salam man {self.name} hastam {self.age}sale az TEH, {self.job} shoghl man hast va dar ,{self.office} kar mikonam')

maryam = Adam('Maryam', 38)
sara = Karmand('Sara', 27, 'computer engineering', 'office A')

maryam.salam()
sara.salam()


