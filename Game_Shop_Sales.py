import pandas as pd
import matplotlib.pyplot as plt
import math 
import numpy 
from datetime import datetime as datetime

df = pd.read_csv("Game_Shop_Sales_300_Rows.csv")



#Data visualisations
def pie_most_popular_games(): # 1
    df = df.groupby("Category")["Units Sold"].sum().to_dict()
 


    plt.pie(df.values() , labels= df.keys())
    plt.title("most popular genres")
    plt.show()

def bar_price_range_compared_to_sales():
    price_range = {"£0-9.99":0 , "£10-19.99":0 , "£20-29.99":0 , "£30-39.99":0 , "£40-49.99":0 ,"£50+":0}

    for i in range(len(df)):
        if float(df["Units Sold"][i]) > float(50):
            price_range["£50+"] = price_range["£50+"] + int(df["Units Sold"][i])
        elif float(df["Units Sold"][i]) > float(39.99):
            price_range["£40-49.99"] = price_range["£40-49.99"] + int(df["Units Sold"][i])
        elif float(df["Units Sold"][i]) > float(29.99):
            price_range["£30-39.99"] = price_range["£30-39.99"] + int(df["Units Sold"][i])
        elif float(df["Units Sold"][i]) > float(19.99):
            price_range["£20-29.99"] = price_range["£20-29.99"] + int(df["Units Sold"][i])
        elif float(df["Units Sold"][i]) > float(10.99):
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
        print(all_game_names)
        print("Enter names of games you would like to see (enter 0 to progress):")

        choice = input(">>")
        #INPUT VALIDATION NEEDED
        choice = str(choice)
        if choice in all_game_names:
            game_names.append( choice)

            print("Accepted. Chosen games:")
            print(game_names)

        elif choice == "0":
            break

        else:
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



line_of_sales_of_each_game()