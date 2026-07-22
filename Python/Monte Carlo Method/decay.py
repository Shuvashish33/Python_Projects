import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

N0 = 1000
lam = 0.1
steps = 100

DK_MC = np.zeros(steps)

N = N0

for t in range(steps):
    decays = np.sum(np.random.random(N) < lam)
    N = N - decays
    DK_MC[t] = N

t_axis = np.arange(steps)
DK_exact = N0 * np.exp(-lam * t_axis)

plt.figure(figsize=(8, 5))

plt.plot(t_axis, DK_MC, "go", markersize=4, label="Monte Carlo Simulation")
plt.plot(t_axis, DK_exact, "r--", linewidth=2, label="Analytical Solution")

plt.title("Radioactive Decay: Monte Carlo vs Analytical Solution")
plt.xlabel("Time Step")
plt.ylabel("Remaining Particles")
plt.grid(True)
plt.legend()

plt.show()