#Euler Method   [1st -while loop, 2nd numpy+for loop] h=1

def euler(x, y, h):
    while x <= 5:
        print(x, "\t\t", y)
        y = y + h * (x**2 + y)
        x+=h

#calling the function
euler(0, 1, 1)



import numpy as np

def euler(x, y, h):
    for x in np.arange(x, 5 + h, h):  # ensures 5 is included
        print(x, "\t", y)
        y = y + h * (x**2 + y)

euler(0, 1, 1)