import numpy as np
from math import*
g=9.8
L=1
def f(t,u,v):
	return v
def b(t,u,v):
	return (-g/L)*sin(u)
def RK4(t0,u0,v0,h):
	t, u, v = t0, u0, v0
	
	for t in np.arange(t,20+h,h):
		print(t,'\t',u,'\t',v)
		
		K1=h*f(t,u,v)
		L1=h*b(t,u,v)
		
		K2=h*f(t+h/2, u+K1/2, v+L1/2)
		L2=h*b(t+h/2, u+K1/2, v+L1/2)
		
		K3=h*f(t+h/2, u+K2/2, v+L2/2)
		L3=h*b(t+h/2, u+K2/2, v+L2/2)
		
		K4=h*f(t+h, u+K3, v+L3)
		L4=h*b(t+h, u+K3, v+L3)
		#
		u=u+(K1+2*K2 +2*K3 + K4)/6
		v=v+ (L1+2*L2 +2*L3 +L4)/6
RK4(0,1,0,0.01)
		
		
		
	