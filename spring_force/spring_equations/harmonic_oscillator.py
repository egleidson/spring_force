import math

def harmonic_oscillator_equation (t1, A, m, k = 50, phi = 0):
    t = t1
    x = []
    omega = (k/m)**0.5
    for i in t:
        X = A * math.cos(omega * i + phi)
        x.append(X)
    return x


def harmonic_oscillator_frequency (m, k = 50):
    f = (1/(2*math.pi))*(k / m)**0.5
    return f

