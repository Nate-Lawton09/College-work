favourite_songs = [0]*5
print("Song name:artist")
for i in range(0,5):
    print((i + 1),"th favoutite song:")
    favourite_songs[i] = str(input(""))



while True:
    favourite_songs.sort()
    print(favourite_songs)
    print("Would you like to append your list")
    x = input("y/n")

    if x == "y" :
        y = str(input("Which item would you like to remove (copy and paste)"))

        favourite_songs.remove(y)


        z = str(input("Enter New item"))

        favourite_songs.append(z)    