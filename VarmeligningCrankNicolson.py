import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

# Definer parameterne


def crank_nicolson(L, t, k, h):
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
        u_values[j+1][0] = 0
        u_values[j+1][NUM_STEPS_X - 1] = 0

        explicit = np.array(u_values[j])

        for i in range(1, NUM_STEPS_X - 1):
            explicit[i] = u_values[j][i] + k / np.power(h, 2) * (u_values[j][i + 1] - 2 * u_values[j][i] + u_values[j][i - 1])

        last_values = np.zeros(NUM_STEPS_X)

        implicit = np.array(u_values[j])

        # Fikspunktiterasjon for å finne implisitt
        while (np.sum(np.abs(last_values - implicit)) > 1e-5):
            last_values = np.array(implicit)
            for i in range(1, NUM_STEPS_X - 1):
                implicit[i] = u_values[j][i]   + k / np.power(h, 2) * (implicit[i + 1] - 2 * implicit[i] + implicit[i - 1])
        
        # Crank Nicolson blir gjennomsnitt av eksplisitt og implisitt
        # Med numpy regner den ut uttrykket for hver [i]
        u_values[j+1] = (explicit + implicit) / 2
    return t_values, x_values, u_values

if __name__ == "__main__":
    L = np.pi
    t = 0.3
    k = 0.001
    h = 0.05
    NUM_STEPS_X = int(L / h)
    NUM_STEPS_T = int(t / k)
    print("Heiii")
    t_values, x_values, u_values = crank_nicolson(L, t, k, h)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(t_values, x_values, u_values, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    plt.show()

    plt.plot(np.arange(0, t, k), u_values[:, NUM_STEPS_X // 2])
    plt.show()