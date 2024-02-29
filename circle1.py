import math

def circumference(area):  
    return(print(math.sqrt(area/math.pi)*math.pi*2))
area = int(input("Area of circle: "))  
circumference(area)
