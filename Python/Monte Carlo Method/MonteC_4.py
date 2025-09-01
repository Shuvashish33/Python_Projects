import numpy as np
N = 20000000
r=int(input("Enter the radius of sphere:")) 
x = np.random.uniform(-r, r, N)
y = np.random.uniform(-r, r, N)
z = np.random.uniform(-r, r, N)
N0= np.sum(x**2 + y**2 + z**2<= r**2)
Volume_sphere= ((2*r)**3 )* N0 /N

print("Estimated the Volume_sphere:",Volume_sphere)




#N0= points inside sphere
#estimate the Volume of any sphere of radius r