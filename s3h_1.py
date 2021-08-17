#BMI=kg/m2
def BMI():
    height =float(input("Enter your height in meters: \n"))
    weight=float(input("Enter your weight in kilograms \n"))
    BMI = weight/height**2
    return BMI
BMI= BMI()
print("Your BMI is:" ,(round(BMI,2)), "kg/m^2")