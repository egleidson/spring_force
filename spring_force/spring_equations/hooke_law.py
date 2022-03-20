def spring_force( x, k = 50 ):
    F = []

    for i in x:
        f = -k*i
        F.append(f)
    return F

def spring_energy (x,k = 50 ):
    U = []

    for i in x :
        u = (1/2) * k * i**2
        U.append(u)
    return U

