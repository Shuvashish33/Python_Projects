from math import *
import numpy as np
def f(x,y):
	return x*sqrt(y)
#calling f function by Creating a RK4 function
def RK4(x,y,h):
        
    for x in np.arange(x,20+h,h):
    	print(round(x,4),'\t',round(y,4))
    	
    	K1=h*f(x,y)
    	K2=h*f(x+h/2 , y+K1/2)
    	K3=h*f(x+h/2,  y+K2/2)
    	K4=h*f(x+h, y+K3)
    	
    	y=y+(K1+2*K2 +2*K3 +K4)/6
RK4(0,1,0.01)




#Actually we're' not calling the f function at that line — but we're defining a new function (RK4) that uses f.
