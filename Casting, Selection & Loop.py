import random
import time
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
        time = time // 60 
        print(time,"hours")
    
    elif x == 2:
        time = time * 60
        print(time,"minutes")
    
def vat_calc():
    bill = input("Total cost without VAT: ") #Bill Williamson?
    bill_vat = int(bill) * 1.2
    vat = bill_vat - int(bill) 
    print("Bill with vat: £", bill_vat)
    print("Vat: £",vat)
    
def pin_check():
    PIN = random.randint(10000,99999)
    attempt = 0
    print("You have a 5 digit pin, get guessing")
    while True:
        attempt = attempt + 1
        guess = int(input(": "))

        if guess == PIN:
            break
        else:
            x = random.randint(1,17)
            if x == 1:
                print("Come on, guess again")
            if x == 2:
                print("Is THAT your best guess?")
            if x == 3:
                print("Im getting bored")
            if x == 4:
                print("*sighs with disapointment")
            if x == 5:
                print("GODD, cant you get anything right")
            if x == 6:
                print("try 12345?")
            if x == 7:
                print("try 45983?")
            if x == 8:
                print("try 65983?")
            if x == 9:
                print("try 85136?")
            if x == 10:
                print("try 94986?")
            if x == 11:
                print("try 34976?")
            if x == 12:
                print("try 34918?")
            if x == 13:
                print("try 10286?")
            if x == 14:
                print("try 29375?")
            if x == 15:
                print("try",PIN,"?")
            if x == 16:
                print("Im waiting")
            if x == 17:
                print("No wonder Hal went rogue if this is how boring humanity is")
            
    if attempts == 1:
        print("WELL DONE")
        print("YOU WIN!!")
        print("Your prize is...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("Nothing!!!!!!")
    print("It took you", attempt, " guesses, loser")

pin_check()