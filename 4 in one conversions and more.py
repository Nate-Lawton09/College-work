import time
def Lab_Results_Unit_Converter():
    Conversion_Rate = 18

    option = int(input("mg/dl to mmol/L (1) or mmol/L to mg/dl (2) or  unkown(3)"))

    if option == 1:
        option = int(input("Enter the amount in mg/dl:"))
        print((option * Conversion_Rate),"mmol/L")

    elif option == 2:
        option = int(input("Enter the amount in mmol/L:"))
        print((option / conversion_rate),"mg/dl")
    
    elif option == 3:
        option = int(input(""))

def average_temperature_tracker():
    Fever_Threshhold = 38
    x = int(input("How many temperatures would you like to enter:"))
    total = 0
    for i in range(x):
        y = int(input("Input temperature:"))
        total = total + y
    
    ave_temp = total / x
    print("Your average temperature is", ave_temp)
    if ave_temp >= Fever_Threshhold:
        print("You have a fever")

def hydration_tracker():
    Daily_Goal = 2000
    total = 0
    day = True
    
    while day == True:
        intake = input("How much water has been darnk in ml (type : end    to end the program)")
        if intake == "end": 
            day = False
        elif intake == "end    to end the program":
            print("Good boy")
            day = False
        else:
            int(intake)
            total = total + intake

    if total == Daily_Goal:
        print("Target met")
    elif total > Daily_Goal:
        print("Target exceeded")
    elif total < Daily_Goal:
        print("Target not met")

def heartrate(): #couldnt fing anything on age:(
    MHR = 220
    LHR = 60
    age = int(input("Enter age:"))
    rhr = int(input("Enter resting heart rate:"))
    if rhr > MHR and rhr < LHR:
        print("This person is dead")
    if rhr > 100:
        print("TOO FAST SEEK HELP")
    if rhr < 60:
        print("this")
        time.sleep(2)
        print("heart")
        time.sleep(2)
        print("rate")
        time.sleep(2)
        print("is")
        time.sleep(2)
        print("too")
        time.sleep(2)
        print("slow")
        time.sleep(2)
        print("seek")
        time.sleep(2)
        print("help")
        


