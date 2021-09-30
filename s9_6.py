class Cars():
    def __init__(self, brand, model, cylinders, currentspeed ):
        
        self.brand = brand
        self.model = model
        self.cylinders = cylinders
        self.currentspeed = currentspeed
        
   
    def gazbede(self):
        
        if int(self.currentspeed) > 60:
            print('police!!!')
        else:
            self.currentspeed +=20
            print("Harekat ba speed {} km/h ".format(self.currentspeed))
        
        
    
    

mycar = Cars("Renault", 2016, 4, 20)

print('gaze 1')
mycar.gazbede()
print('gaze 2')
mycar.gazbede()
print('gaze 3')
mycar.gazbede()
print('gaze 4')
mycar.gazbede()
