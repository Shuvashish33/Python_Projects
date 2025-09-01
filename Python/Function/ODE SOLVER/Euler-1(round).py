#Euler Method   [1st -while loop, 2nd numpy+for loop]

def euler(x, y, h):
    while x <= 5:
        print(round(x,3), "\t\t", round(y,3))
        y = y + h * (x**2 + y)
        x+=h

#calling the function
euler(0, 1, 0.1)



import numpy as np

def euler(x, y, h):
    for x in np.arange(x, 5 + h, h):  # ensures 5 is included
        print(round(x,3), "\n\t\t", round(y,3))
        y = y + h * (x**2 + y)

euler(0, 1, 0.1)