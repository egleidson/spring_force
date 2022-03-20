import matplotlib.pyplot as plt
import random
import math


def plot_harmonic(m,k = 50,A):
    x = []
    omega = (k / m) ** 0.5
    t = []
    while len(t) <= 10:
        t_i = random.randint(0, 10)
        if t_i not in t:
            t.append(t_i)
            t.sort()

    for i in t:
        X = A * math.cos(omega * i)
        x.append(X)
        # y.append(next(h))

    plt.plot(t, x)



