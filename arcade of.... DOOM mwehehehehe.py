arcade = {
    "pinball wizard" : {"Category":"pinball" , "Status":"working"},
    "devil may cry" : {"Category":"battle" , "Status":"out of order"}
}

print(arcade)


#  change status

def status_append():

    print("Enter name of game:")
    x = str(input(""))
    x.lower()

    print("Enter new status:")
    y = str(input(""))
    y.lower

    arcade[x]["Status"] = {y}

    print("Updated list")
    print(arcade)

# add new 

def add() :

    print("Enter name of new machine:")
    x = str(input(""))
    x.lower()

    print("Enter category of new machine:")
    y = str(input(""))
    y.lower

    print("Enter status of new machine")
    z = str(input(""))
    z.lower

    arcade[x] = {"Category": y , "Status":z }
    print(arcade)


# status search
def status_search():
    print("What status would you like to see:")
    x = str(input(""))
    x.lower

    for i in range(len(arcade)):
        arcadeName = list(arcade.keys())[i]

        if arcade[arcadeName]["Status"] == x:
            print(arcadeName)
   
    

# choices loop

while True:
    print("Functions: Update machine status (1) / Add new machine (2) / Search by Status (3)")
    choice = int(input(""))

    if choice == 1:
        status_append()

    if choice == 2:
        add()
    
    if choice == 3:
        status_search()