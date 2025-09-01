import numpy as np
N = 20000000
x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)
z = np.random.uniform(-1, 1, N)
inside_sphere= np.sum(x**2 + y**2 + z**2<= 1)
pi_estimate = (6 * inside_sphere )/N

print("Estimated value of Pi:",pi_estimate)




#inside_sphere=N0
#estimate pi from unit sphere