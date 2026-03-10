import pandas as pd
import matplotlib.pyplot as plt
import math 
import numpy as np 
from datetime import datetime as datetime

df = pd.read_csv("Game_Shop_Sales_300_Rows.csv")



#Data visualisations
def pie_most_popular_games(): # 1
    df = df.groupby("Category")["Units Sold"].sum().to_dict()
 


    plt.pie(df.values() , labels= df.keys())
    plt.title("most popular genres")
    plt.show()

def bar_price_range_compared_to_sales():
    price_range = {"£0-9.99":0 , "£10-19.99":0 , "£20-29.99":0 , "£30-39.99":0 , "£40-49.99":0 , "£50-59.99":0 ,"£60+":0}

    for i in range(len(df)):
        if float(df["Price"][i]) > float(60):
            price_range["£60+"] = price_range["£60+"] + int(df["Units Sold"][i])
        elif float(df["Price"][i]) > float(49.99):
            price_range["£50-59.99"] = price_range["£50-59.99"] + int(df["Units Sold"][i])
        elif float(df["Price"][i]) > float(39.99):
            price_range["£40-49.99"] = price_range["£40-49.99"] + int(df["Units Sold"][i])
        elif float(df["Price"][i]) > float(29.99):
            price_range["£30-39.99"] = price_range["£30-39.99"] + int(df["Units Sold"][i])
        elif float(df["Price"][i]) > float(19.99):
            price_range["£20-29.99"] = price_range["£20-29.99"] + int(df["Units Sold"][i])
        elif float(df["Price"][i]) > float(10.99):
            price_range["£10-19.99"] = price_range["£10-19.99"] + int(df["Units Sold"][i])
        else:
            price_range["£0-9.99"] = price_range["£0-9.99"] + int(df["Units Sold"][i])
    print(price_range)

    plt.bar(price_range.keys() , price_range.values()) 
    plt.title("Number of sales from each game")
    plt.xlabel("Price ranges")
    plt.ylabel("Number of sales")
    plt.show()



def line_of_sales_of_each_game():
    

    all_game_names = df["Game Title"].drop_duplicates().to_list()
    dates = df["Date"].drop_duplicates().to_list()
    game_names = []

    while True:
        
        """print(f"Earliest Date: {dates[0]} \nFinal Date: {dates[-1]}")
        while True:
            print("Enter start date:")
            start_date = input(">>")
            if start_date not in dates:
                print("Date not found")
            else:
                start_index = dates.index(start_date)
                break
        
        while True:
            print("Enter end date:")
            end_date = input(">>")
            if end_date not in dates:
                print("Date not found")        
            else:
                end_index = dates.index(end_date)
                break

        for i in range(len(dates)):
            if i > start_index or i < end_index:
                dates = dates.remove(dates[i])"""
        
        

        
        print(all_game_names)
        print("Enter names of games you would like to see (enter 0 to progress):")

        choice = input(">>")
        
        choice = str(choice)

        valid = False

        for i in range(len(all_game_names)):
            if all_game_names[i].lower() == choice.lower():
                valid = True
                break
            else:
                valid = False
        
        if valid == True:
            game_names.append( choice)

            print("Accepted. Chosen games:")
            print(game_names)

        elif choice == "0":
            break

        elif valid == False:
            print("Game not found")

    
    game_sales = {}

    for x in range(len(game_names)):
        game_sales[game_names[x]] = {}  
        for y in range(len(dates)):
            game_sales[game_names[x]][dates[y]] = 0
    
    
    for i in range(len(df)):
        
        for x in range(len(game_names)):
            
            if df["Game Title"][i] == game_names[x]:
                game_sales[game_names[x]][df["Date"][i]] = df["Units Sold"][i]

    
    

                
    
   
    
    
    for i in game_sales:
        plt.plot(game_sales[i].keys(), game_sales[i].values())
        #plt.plot(dates , game_sales[i].values())
        

    plt.grid(True, linestyle='--', linewidth=0.7)
    plt.legend(game_names)
    plt.title("Sales of each game over time")
    plt.ylabel("Dates")
    plt.ylabel("Sales")

    plt.show()




def calculate_total():
    all_game_names = df["Game Title"].drop_duplicates().to_list()
    print(all_game_names)
    print("Enter names of games you would like to see (enter 0 to progress):")

    choice = input(">>")
    #Validate input
    choice = str(choice)
    valid = False
    for i in range(len(all_game_names)):
            
            if all_game_names[i].lower() == choice.lower():
                valid = True
                break
            else:
                valid = False
    if valid == True:
        chosen_game = choice

        total = 0

        for i in range(len(df)):
            if df["Game Title"][i] == chosen_game:
                total = np.add(df["Total Revenue"][i] , total)
                total = np.round(total ,  decimals = 2)
            
        print(f"{chosen_game} had a total of £{total} in revenue")
    
    else:
        print("Game Not found")

def total_copies():
    total = 0
    for i in range(len(df)):
        total = np.add(total , df["Units Sold"][i])

    print(f"A total of {total} games were sold")
####################
def main_menu():

    while True:
        choice = input(">>")

        try:
            int(choice)
        except:
            print("Invalid input")
        else:
            break
    
    return choice
    

print("#" * 30)
print("#" ,"Welcome to Shop Sales" ,"#")
print("#" * 30)
print("## 1 . View line chart of game sales over time")
print("## 2 . View bar chart of Prices compared to number of sales")
print("## 3 . View pie chart of game categories")
print("## 4 . Calculate total revenue from a game")
print("## 5 . Calculate How many games sold in total")

choice = main_menu()

if choice == "1":
    line_of_sales_of_each_game()

if choice == "2":
    bar_price_range_compared_to_sales()

if choice == "3":
    pie_most_popular_games()

if choice == "4":
    calculate_total()

if choice == "5":
    total_copies()

else:
    print("Sorry, you have not selected a valid option")
