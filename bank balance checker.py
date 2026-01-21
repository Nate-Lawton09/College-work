import random
easteregg = random.randint(1,500)
if easteregg == 67:
    input("Whats that funny long number on the back of your credit card?")
    input("whats the name on the back?")
    input("whats the 3 digit number on the back")

balance = input("How much money was in your bank account at the begining of the day:")
withdrawl = input("How much money has exited your bank account today?")
increase = input("How much money entered your account today?")

balance = balance - withdrawl
balance = balance + increase

print("Your new balance is:",balance)