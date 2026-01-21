alphabet = [
    "A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h",
    "I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p",
    "Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x",
    "Y","y","Z","z",
    "0","1","2","3","4","5","6","7","8","9",
    ".", ",", "!", "?", ":", ";", "'", "\"",
    "+", "-", "*", "/", "=", "%",
    "(", ")", "[", "]", "{", "}",
    "@", "#", "$", "&", "_", "~",
    "<", ">", "^", "|", " "
]

cypher = [
    "H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o",
    "P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w",
    "X","x","Y","y","Z","z","A","a","B","b","C","c","D","d","E","e",
    "F","f","G","g",

    "5","6","7","8","9","0","1","2","3","4",

    ".", ",", "!", "?", ":", ";", "'", "\"",

    "+", "-", "*", "/", "=", "%",

    "(", ")", "[", "]", "{", "}",

    "@", "#", "$", "&", "_", "~",

    "<", ">", "^", "|", " "
]



def encode():
    print("Enter message:")
    entry = str(input(""))
    added = False
    encoded_message = ""
    broken = list(entry)
    for i in range(len(entry)):
        added = False
        x = broken[i]

        for c in range(len(alphabet)):
            if x == alphabet[c]:
                encoded_message = encoded_message + cypher[c]
                added = True
    
        if added == False:
            encoded_message = encoded_message + x



    print(encoded_message)

def decode():
    print("Enter message:")
    entry = str(input(""))
    added = False
    decoded_message = ""
    broken = list(entry)
    for i in range(len(entry)):
        added = False
        x = broken[i]

        for c in range(len(alphabet)):
            if x == cypher[c]:
                decoded_message = decoded_message + alphabet[c]
                added = True
    
        if added == False:
            decoded_message = decoded_message + x



    print(decoded_message)

def reset_cypher():

    cypher = [0] * len(alphabet)

    for i in range(cypher):
        print(f"{alphabet[i]} = ")
        x = input("")

        for c in range(cypher):
            if x == cypher(c):
                print("Already used")
                while True:
                    print(f"{alphabet[i]} = ")
                    x = input("")
                    if x != cypher[c]:
                        break
        cypher[i] = x

while True:
    print("Decode - 1")
    print("Encode - 2")
    print("Reset cypher - 3")
    choice = int(input(""))

    if choice == 1:
        decode()
    if choice == 2:
        encode()
    if choice == 3:
        cypher()