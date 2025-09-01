import numpy as np
from math import *
def RK1(x,y,h):
	for x in np.arange(x, 5+h ,h):
		print(x,'\t', y)
		y=y+h*(y-0.5*exp(x/2) * sin(5*x)+5*exp(x/2) *cos(5*x))

RK1(0,0,0.1)