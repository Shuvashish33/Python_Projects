import numpy as np
N = 20000000 
x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)
z = np.random.uniform(-1, 1, N)
N0= np.sum(x**2 + y**2 + z**2<= 1)
Volume_sphere= (8 * N0 )/N

print("Estimated the Volume_sphere:",Volume_sphere)




#N0= points inside sphere
#estimate the Volume of a unit sphere