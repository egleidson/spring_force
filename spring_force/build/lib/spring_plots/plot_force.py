from matplotlib import pyplot as plt
import random


def plot_hooke_force(k):
    F = []
    x = []


    while len(x) <= 100:
        x_i = random.randint(0, 100)
        if x_i not in x:
            x.append(x_i)
            x.sort()

    for i in x:
        f = -k * i
        F.append(f)

    plt.plot(x, F)
