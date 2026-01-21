def wth():
    energy = [1,27,50,67,100]
    usernames = ["Fitness_Faye","Athletic_Alison","Jumping_Julie","Smoothies_Sabrina"]

    print(energy)
    print(energy[0])
    print(energy[-1])
    print(energy[len(energy) // 2])

def im_working_on_it():
    screentimes = [120,95,140,160,80,100,200]
    print(screentimes)
    print(screentimes[2])
    print(screentimes[(0+1+2)//3])
    screentimes[-1] = 250
    print(screentimes)
    print(min(screentimes))
    print(max(screentimes))


def investigate():
    listA = [1,2,3]
    listB = [1,"2",3]

    print(listA)
    print(listB)


def notifications():
    notifs = [34 , 42 ,67 , 69 , 21, 66 ,36]

    print(notifs)
    print(min(notifs))
    print(max(notifs))

    for i in range(0,notifs):
        total = total + notifs[i]
    
    print(total)
    print(total//len(notifs))

    print("input the new number:")
    x = int(input(""))

    notifs.append(x)
    print(notifs)

    notifs2 = [42 , 24 ,67 , 96, 12, 67 ,63]

    print(notifs2)
    print(min(notifs2))
    print(max(notifs2))

    for i in range(0,notifs2):
        total2 = total2 + notifs2[i]
    
    print(total2)
    print(total2//len(notifs2))

    print("input the new number:")
    x = int(input(""))

    notifs.append(x)
    print(notifs2)




