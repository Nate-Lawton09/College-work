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

total_patients = 0

def add_patient():
    global total_patients
    total_patients += 1
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    print("Patient added:", name)

def view_total():
    print("Total patients:", total_patients)
    

while True:
    choice = input("recordfiles (1), bmi (2), doseage (3), record a new patient (4), view patients (5), exit (6) ")


    if int(choice) == 1:
        ehr()
    if int(choice) == 2:
        bmi_calculator()
    if int(choice) == 3:
        dose_limit()
    if int(choice) == 4:
        add_patient()
    if int(choice) == 5:
        view_total()
    if int(choice) == 6:
        break
print("Thanks")
