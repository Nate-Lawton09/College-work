def arithmetic_basics():
    Goal = 10000
    steps = int(input("Enter the number of steps you walked:"))
    Percent_Complete = round((steps/Goal) * 100)
    Remainder = Goal - steps

    if steps >= Goal:
        print("Goal reached")
    
    else:
        print("Steps remainding:", Remainder)
        print(Percent_Complete," percentage completed")

def bmi_buckets():
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

def Screen_time_flag():
    daily_screen_minutes = int(input("How many minutes do you spend on the screen today:"))
    nightly_screen_minutes = int(input("How many minutes do you spend on the screen tonight:"))
    steps = int(input("Number of steps:"))

    flag = False

    if daily_screen_minutes > 240 and (nightly_screen_minutes > 60 or steps < 5000):
        print("You are being flagged")
        flag = True

def hydration_steak(): 
    print("mmmmmmmmmmm water")

    water = int(input("waterintake in ml:"))
    points = water//250
    bonus = (water//2000)*5
    points = points + bonus
    print("You gained", points , "points") 


def eligibility_for_free_class():
    days_since_last_free_class = int(input("Days since last free class:"))
    
    if days_since_last_free_class >30:
        days_since_last_free_class_verification_check = True
    
    age = int(input("Age:"))

    if age > 16 and age < 25:
        age_verification_check = True
    
    income = int(input("What is your annual income:"))

    if income < 20000:
        income_verification_check = True

    if days_since_last_free_class_verification_check == True and age_verification_check == True and income_verification_check == True:
        print("Your eligable for a free class")

def tiered_awards():
    steps = int(input("Enter number of steps:"))
    water = int(input("Enter amount of water consumed in ml:"))
    points = (steps//1000)*2 + (water//500)

    if points <= 19 :
        bronze = True
    elif points <= 39:
        silver = True
    else:
        gold = True

def division_and_rounding():
    sessions = int(input("Number of sessions:"))
    minutes = int(input("Total number of minutes across all sessions"))
    avg_session_length = minutes / sessions
    safe_avg_session_length = round(avg_session_length,1)
    print(safe_avg_session_length)

