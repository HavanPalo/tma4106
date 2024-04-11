import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

# Definer parameterne

def implisitt(L, t, k, h):
    NUM_STEPS_X = int(L / h)
    NUM_STEPS_T = int(t / k)

    x_values = np.linspace(0, L, NUM_STEPS_X)
    t_values = np.linspace(0, t, NUM_STEPS_T)

    u_values = np.zeros((NUM_STEPS_T, NUM_STEPS_X))
    u_values[0] = np.sin(x_values) #initialbetingelse

    x_values, t_values = np.meshgrid(x_values, t_values)
    # sett opp initialverdier i u_values
    # sett opp u_values[0] - arrayen 

    # x_values = np.linspace(0, L, NUM_STEPS_X)

    for j in range(NUM_STEPS_T - 1):
        # Randkrav
        u_values[j+1][0] = 0
        u_values[j+1][NUM_STEPS_X - 1] = 0

        # Fikspunkt iterasjon
        u_values[j + 1] = np.array(u_values[j])
        last_values = np.zeros(NUM_STEPS_X)

        while (np.sum(np.abs(last_values - u_values[j + 1])) > 1e-8):
            last_values = np.array(u_values[j + 1])
            for i in range(1, NUM_STEPS_X - 1):
                u_values[j + 1][i] = u_values[j][i] + k / np.power(h, 2) * (u_values[j + 1][i + 1] - 2 * u_values[j + 1][i] + u_values[j+1][i - 1])
    return t_values, x_values, u_values

if __name__ == "__main__":
    L = np.pi
    t = 0.3
    k = 0.001
    h = 0.05

    t_values, x_values, u_values = implisitt(L, t, k, h)
            
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(t_values, x_values, u_values, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    plt.show()