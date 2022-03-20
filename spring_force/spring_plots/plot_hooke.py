from matplotlib import pyplot as plt
import random


def plot_hooke(k = 50):
    F = []
    x = []


    while len(x) <= 10:
        x_i = random.randint(0, 10)
        if x_i not in x:
            x.append(x_i)
            x.sort()

    for i in x:
        f = -k * i
        F.append(f)

    plt.plot(x, F)