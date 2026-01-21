import matplotlib.pyplot as plt 

a = (6)
b = (1,3,9,10,4,22)
c = (1,2,3,4,5,6)
plt.style.use('./images/Theo.JPG')

plt.bar(c,b)

plt.title("Dave")
plt.xlabel("hours played")
plt.ylabel("enemies felled")
plt.grid()
print(plt.style.available)


plt.show()
