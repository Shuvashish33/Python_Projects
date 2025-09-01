import numpy as np
N = 10000000
x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)
inside_circle= np.sum(x**2 + y**2 <= 1)
pi_estimate = (4 * inside_circle)/N

print("Estimated value of Pi:",pi_estimate)




#inside_circle=N0
#estimate pi from unit circle