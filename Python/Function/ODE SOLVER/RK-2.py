import numpy as np
def RK2(x,y,h):
	for x in np.arange(x,5+h,h):
		print(x,'\t',y)
		k1=h*(x**2+y)
		k2=h*((x+h)**2 + y+k1)
		y=y+0.5*(k1+k2)
RK2(0,1,0.1)


#y'=x²+y