average = [0]*10
for i in range(10):
    looper = int(input("Enter the number of tests:"))
    total = 0
    for i in range(looper):
        score = int(input("Enter score:"))
        total = total + score
        

    average[i] = total / looper
    print("the average score was:", average[i])
    print(type(average[i]))

x= int(input("Which set would you like to access?"))
print("the average score was:", average[x])

