from math import *
import numpy as np
def f(x,y):
	return x*sqrt(y)
def RK4(x0,y0,h):
    x=x0       #x update value, x0 intial value
    y=y0       # same for y
    for x in np.arange(x,20+h,h):
    	print(round(x,4),'\t',round(y,4))
    	
    	K1=h*f(x,y)
    	K2=h*f(x+h/2 , y+K1/2)
    	K3=h*f(x+h/2,  y+K2/2)
    	K4=h*f(x+h, y+K3)
    	
    	y=y+(K1+2*K2 +2*K3 +K4)/6
RK4(0,1,0.01)

#x=x0, y=0 used to separate the Initial Condition From Updating Value, So That If We Need To Extend The Code For Some Reason(Eg:Plotting) And That Time If we require the initial value ,then that case we won't be able to access the initial value(Condition) again



