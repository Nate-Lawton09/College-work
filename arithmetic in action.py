def calorie_burn():
    calories = int(input("How many calories have you consummed per minute:"))
    workout_time = int(input("Time in minutes spent working out:"))
    burnt = calories/workout_time
    print("You burnt",burnt,"calories")

def step_converter():
    steps = int(input("How many steps have you walked:"))
    Steps_In_A_KM = 1300

    distance_walked = steps / Steps_In_A_KM 
    print("you walked",distance_walked,"KM")

def medication_timing():
    time = int(input("Enter time between medication in minutes:"))
    hours = time // 60
    minutes = time % 60

    print("Time between medication is:",hours,"hours and",minutes,"minutes")

def pack_usage():
    total = int(input("Enter total number of tablets"))
    Per_Pack = int(input("Home many in a pack?"))

    left_over = total % Per_Pack
    packs = total // Per_Pack

    print("They're are ",packs," total packs and ",left_over," tablets remaining")

def heart_recovery():
    heart_rate = int(input("Enter your natural heart rate"))
    rate = heart_rate * (0.9 ** 5)
    print ("It will take ", rate ,"Seconds to return to normal")


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
    choice = input("recordfiles (1), bmi (2), doseage (3), record a new patient (4), view patients (5), calorie burner (6), step converter (7), Medication timing (8), Pack maker (9), Heart rate recovery (10), exit (11) ")


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
        calorie_burn()
    if int(choice) == 7:
        step_converter()
    if int(choice) == 8:
        medication_timing()
    if int(choice) == 9:
        pack_usage()
    if int(choice) == 10:
        heart_recovery()
    if int(choice) == 11:
        break
print("Thanks")

