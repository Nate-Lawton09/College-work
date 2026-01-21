def ehr ():
    Name = str(input("Enter Name:"))
    Date_Of_Birth = input("Enter Date of birth (dd/mm/yyyy):")
    Age = input("Enter age:")
    Height = input("Enter height(x feet, y inches):")

    print(Name, ",", Date_Of_Birth, ",", Age,"years old,", Height) 

def bmi_calculator () :
    weight = float(input("Weight in kg:"))
    height = float(input("Height in Meters:"))

    height_squared = height * height 

    bmi = weight / height_squared

    if bmi < 18.5:
        print("Underweight")
    elif bmi < 24.9:
        print("Healthy weight")
    elif bmi < 29.9:
        print("Overweight")
    elif bmi < 39.9:
        print("obese")
    else:
        print("severe obesity")

def dose_limit ():
    maximumdose = int(input("Enter Maximum allowed dossage in mg:"))
    total = 0

    while total < maximumdose:
        total = total + int(input("Enter dosage:"))
        if total > maximumdose:
            print("Exceeds maximum allowed dosage")
            print((maximumdose - total), "mg allowed left for the day" )
        else:
            print("dosage allowed")
    print("Maximum dosage reached")

def bill ():
    room = int(input("How much is the room?"))
    treatment = int(input("How much was treatment?"))
    consults = int(input("How much was consultations?"))
    total = (room + treatment + consults) * 1.2
    print("Your total bill is £",total) 
    

while True:
    choice = int(input("recordfiles (1), bmi (2), doseage (3), bill (4) "))

    if choice == 1:
        ehr()
    if choice == 2:
        bmi_calculator()
    if choice == 3:
        dose_limit()
    if choice == 4:
        bill()
