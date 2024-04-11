from VarmeligningCrankNicolson import crank_nicolson
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from VarmeligningImplisitt import implisitt
from VarmeligningEksplisitt import eksplisitt


if __name__ == "__main__":
    L = np.pi
    t = 1
    k = 0.001
    h = 0.1

    NUM_STEPS_X = int(L / h)
    NUM_STEPS_T = int(t / k)
    t_values, x_values, u_values = crank_nicolson(L, t, k, h)
    t_values, x_values, u1_values = implisitt(L, t, k, h)
    t_values, x_values, u2_values = eksplisitt(L, t, k, h)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    surf = ax.plot_surface(t_values, x_values, u_values, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    surf = ax.plot_surface(t_values, x_values, u1_values, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    surf = ax.plot_surface(t_values, x_values, u2_values, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    plt.show()

    x_point = NUM_STEPS_X // 2
    x_val = x_values[0, x_point-1]
    analytic = np.exp(-np.arange(0, t, k)) * np.sin(x_val)

    plt.plot(np.arange(0, t, k), u_values[:, x_point], label="crank nicolson")
    plt.plot(np.arange(0, t, k), u1_values[:, x_point], label="implisitt")
    plt.plot(np.arange(0, t, k), u2_values[:, x_point], label="eksplisitt")
    plt.plot(np.arange(0, t, k), analytic, label="analytisk")
    plt.legend()
    plt.show()