def rectangle_area():
    length = int(input("Enter length of rectangle: "))
    height = int(input("Enter height of rectangle: "))
    unit = str(input("Enter unit of measurement"))

    area = length * height

    if length == height:
        print("Thats a square")
    print("Area of shape is: ", area, unit)

def hours_to_min():
    x = int(input("Enter units in minutes (1) or hours (2)?"))
    
    time = int(input("Enter amount of time: "))

    if x == 1:
        time = time // 60 + time % 60
        print(time,"hours")
    
    elif x == 2:
        time = time * 60
        print(time,"minutes")
    
hours_to_min()