conversion = input("Do you wish to convert a value into celsius (1) or Farenheight (2)")
temp = int(input("input temperature"))
if conversion == 1:
    ans = conversion - 32
    ans = ans * 5
    ans = ans / 9

elif conversion == 2:
    ans = conversion * 9
    ans = ans / 5
    ans = ans + 32

print(ans)