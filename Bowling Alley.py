import random
Price_Of_Bowling_PP = 12.50
number_of_bowlers = 0
total = 0
cafe_total = 0
bowling_total = 0

sale_complete = False
bowling = False
paid = False


cafe = {"fries":{"Price":2.00},
        "cheese burger":{"Price":6.50},
        "hot dog" : {"Price": 6.00},
        "block'o'cheese" : {"Price":67.00},
        "hot drink" : {"Price":1.50},
        "cold drink" : {"Price":1.00}

        }

times = {"days":{
    "mon": {
        "11:00": False, "11:30": False,
        "12:00": False, "12:30": False,
        "13:00": False, "13:30": False,
        "14:00": False, "14:30": False,
        "15:00": False, "15:30": False,
        "16:00": False, "16:30": False,
        "17:00": False, "17:30": False,
        "18:00": False, "18:30": False,
        "19:00": False, "19:30": False,
        "20:00": False, "20:30": False,
        "21:00": False, "21:30": False,
        "22:00": False
    },
    "tue": {
        "11:00": False, "11:30": False,
        "12:00": False, "12:30": False,
        "13:00": False, "13:30": False,
        "14:00": False, "14:30": False,
        "15:00": False, "15:30": False,
        "16:00": False, "16:30": False,
        "17:00": False, "17:30": False,
        "18:00": False, "18:30": False,
        "19:00": False, "19:30": False,
        "20:00": False, "20:30": False,
        "21:00": False, "21:30": False,
        "22:00": False
    },
    "wed": {
        "11:00": False, "11:30": False,
        "12:00": False, "12:30": False,
        "13:00": False, "13:30": False,
        "14:00": False, "14:30": False,
        "15:00": False, "15:30": False,
        "16:00": False, "16:30": False,
        "17:00": False, "17:30": False,
        "18:00": False, "18:30": False,
        "19:00": False, "19:30": False,
        "20:00": False, "20:30": False,
        "21:00": False, "21:30": False,
        "22:00": False
    },
    "thu": {
        "11:00": False, "11:30": False,
        "12:00": False, "12:30": False,
        "13:00": False, "13:30": False,
        "14:00": False, "14:30": False,
        "15:00": False, "15:30": False,
        "16:00": False, "16:30": False,
        "17:00": False, "17:30": False,
        "18:00": False, "18:30": False,
        "19:00": False, "19:30": False,
        "20:00": False, "20:30": False,
        "21:00": False, "21:30": False,
        "22:00": False
    },
    "fri": {
        "11:00": False, "11:30": False,
        "12:00": False, "12:30": False,
        "13:00": False, "13:30": False,
        "14:00": False, "14:30": False,
        "15:00": False, "15:30": False,
        "16:00": False, "16:30": False,
        "17:00": False, "17:30": False,
        "18:00": False, "18:30": False,
        "19:00": False, "19:30": False,
        "20:00": False, "20:30": False,
        "21:00": False, "21:30": False,
        "22:00": False
    },
    "sat": {
        "11:00": False, "11:30": False,
        "12:00": False, "12:30": False,
        "13:00": False, "13:30": False,
        "14:00": False, "14:30": False,
        "15:00": False, "15:30": False,
        "16:00": False, "16:30": False,
        "17:00": False, "17:30": False,
        "18:00": False, "18:30": False,
        "19:00": False, "19:30": False,
        "20:00": False, "20:30": False,
        "21:00": False, "21:30": False,
        "22:00": False
    }}
}

def bowling_party_discount():
    global bowling_total
    if number_of_bowlers >= 5 :
        bowling_total = bowling_total * 0.8
        print("Discount applied")



def time_check():
    global times
    print("==========================")
    print("Please select the day (Mon-Sat)")
    x = input("")
    if x.lower() not in times["days"]:
        while True:
            print("Invalid day. Try again:")
            x = input("")
            if x.lower() in times["days"]:
                break
    print("Please select one of the available times (hr:min):")
    print(times["days"][x])
    y = input("")
    if times["days"][x][y] == False:
        print("Valid booking")
        times["days"][x][y] = True
    else:
       
        while times["days"][x][y] != False:
            y = input("")
            print("Invalid booking. Select a time labelled False")
     

def book_bowling():


    global number_of_bowlers , bowling_total , Price_Of_Bowling_PP , bowling
    print("==========================")
    print("How many people will be bowling with you?")
    number_of_bowlers = int(input(""))
    bowling_total = number_of_bowlers * Price_Of_Bowling_PP + bowling_total
    time_check()
    bowling_party_discount()
    print("Bowling Total: £",bowling_total)
    bowling == True

def totalling():
    print("Calculating total bill")
    print("==========================")
    print("Total cost of bowling: £",bowling_total)
    print("Total cost of cafe: £",cafe_total )
    total = cafe_total + bowling_total
    print("")
    print("Total bill: £",total)
    print("Is customer ready to pay?")
    x = input("y/n")

    if x.lower() != "y" and x.lower() != "n":
        while True:
            print("Invalid input. Please retry")
            x = input("y/n")
            if x.lower() == "y" or x.lower() == "n":
                break
    
    if x.lower == "n":
        print("Returning to menu")
    
    elif x.lower == "y":
        while paid == False:
            print("Has customer paid yet?")
            x = input("y/n")

            if x.lower() != "y" and x.lower() != "n":
                while True:
                    print("Invalid input. Please retry")
                    x = input("y/n")
                    if x.lower() == "y" or x.lower() == "n":
                        break
        
            if x.lower == "y":
                print("Transaction complete")
                sale_complete = True
                paid = True
            if x.lower() == "n":
                print("Awaiting Customer payment")    


def system_loop():
    sale_complete = False
    print("Would you like to start a new order?")
    x = input("y/n").lower()

    if x.lower() != "y" and x.lower() != "n":
        while True:

            print("Input invalid. Try again")
            x = input("y/n").lower()
            if x.lower() == "y" or x.lower() == "n":
                break
    
    if x == "n":
        print("Then why did you look at the system? Moron")

    if x == "y":
        while sale_complete == False:
            print("==========================")
            print("Please select action:")
            print("Create a bowling party (1)")
            print("Create a cafe order (2)")
            print("Cancel (3)")
            print("Check out (4)")
            x = int(input(""))

            if x < 1 or x > 4:
                while True:
                    print("Invalid input. Please retry")
                    x = int(input(""))

            if x == 1 and bowling == False:
                book_bowling()
            
            if x == 1 and bowling == True:
                print("==========================")
                print("You have already booked a bowling party.")
                print("Are you sure you would like to book another?")
                x = input("y/n")
                if x.lower() == "y":
                    book_bowling()
                else:
                    print("EXTRA BOWLING PARTY CANCELLED")
            
            if x == 2:
                print("==========================")
                print("Menu:")
                print(cafe)
                print("==========================")
                print("Enter what you would like to order. Press enter to confirm. Type END to exit.")

                while True:
                    x = input("Order:")
                    if x == "END":
                        break
                    if x.lower() != cafe:
                        print("Invalid Menu Item")

                    else:
                        cafe_total = cafe_total + cafe[x]["Price"]
                        print("Cafe total: £",cafe_total)
            
            if x == 3:
                print("Are you sure you want to cancel this order?")
                x = input("Press y to confirm")

                if x.lower() == "y":
                    print("ORDER CANCELLED")
                    sale_complete = False

                else:
                    print("==========================")
            
            if x == 4:
                print("==========================")
                totalling()

while True:
    break
    system_loop()
    
############################################################################################################
log_in = False
first_name = ["Kye"]
surname = ["Taylor"]
employee_id = ["6767"]

def enter_new_employee():
    name = input("Enter first name:")
    last_name = input("Enter Surname:")
    idnumber = random.randint(1000,9999)

    if idnumber in employee_id:
        while idnumber in employee_id:
            idnumber = random.randint(1000,9999)

    first_name.append(name) 
    surname.append(last_name) 
    employee_id.append(idnumber) 
    print("Employee id number:",idnumber)

def view_employees():
    for i in range(0,len(first_name)):
        print("employee:", first_name[i],"",surname[i]," Number:",employee_id[i])

def user_check():
    print("Enter User ID:")
    x = input("")

    if x in employee_id:
        print("Access Granted")
        log_in = True
        system_loop()
    else:
        print("Acess Denied") 


############################################################################################################
while True:
    print("==========================")
    print("Choose action:")
    print("Enter a new employee (1)")
    print("View existing employees (2)")
    print("Log in / start a sale (3)")
    x = int(input(""))
    
    if int(x) < 1 or int(x) > 3 :
        print("Invalid input")
    
    if int(x) == 1:
        enter_new_employee()
    if int(x) == 2:
        view_employees()
    if int(x) == 3:
        user_check()

        if log_in == True:
            system_loop()



