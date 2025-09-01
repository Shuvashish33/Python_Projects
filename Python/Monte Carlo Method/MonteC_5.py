import numpy as np
r=int(input("Enter the radius of circle:"))
N=1000000
x=np.random.uniform(-r,r, N)
y=np.random.uniform(-r,r, N)
N0=np.sum(x**2 +y**2 <=r**2)

A_circle=((2*r)**2 )*N0 / N 
print("\nArea of circle=",A_circle)

#area of any circle