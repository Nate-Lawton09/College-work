films = ["Eldenring - the movie","Darksouls4 - return of the souls","Slow and calm","5 nights at Freddy krugers","A christmas Carol"]




while True:
    films.sort()
    print(films)
    print("Would you like to append your list")
    x = input("y/n")

    if x == "y" :
        y = str(input("Which item would you like to remove (copy and paste)"))

        films.remove(y)


        z = str(input("Enter New item"))

        films.append(z)    