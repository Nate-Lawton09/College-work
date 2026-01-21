pay_plan = False
NAME = input("Enter patient name: ")
AGE = int(input("Enter patient age: "))
bill = int(input("Enter total cost of bill: "))

if AGE < 18 : 
    print("Discount applied. 20 percent off")
    bill = bill * 0.8 

if bill > 1000:
    pay_plan = True

print("Your final bill is: $", bill)

if pay_plan == True:
    x = int(input("Would you like the 1 year, 5 year or 10 year plan"))
    
    payments = bill / (x*12)
        
    print("Monthly installments of",payments,"for", (x * 12), "months.")