def Area():
    
    length=float(input("Enter the length: \n"))
    width=float(input("Enter the width: \n"))
    unit=str(input("Enter the unit of the variable: \n"))
    
    if unit=="meter"  or unit=="Meter" or unit=="m" :
        Area=length*width
        return Area
    elif unit=="centimeter"  or unit=="Centimeter" or unit=="cm" :
        Area=(length/100)*(width/100)
        return Area
    elif unit=="millimeter"  or unit=="Millimeter" or unit=="mm" :
        Area=(length/1000)*(width/1000)
        return Area
    else:
        Area=length*width
        return Area
Area=Area()
print("Area is" ,round(Area,4), "m^2" )
        