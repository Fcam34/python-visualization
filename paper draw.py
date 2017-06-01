import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
def f1(z, c=0.285+0j):
    return z**3 + c/(z**3)
def f2(z, c=0+0.1j):
    return z**3 + c/(z**3)
def f3(z, c=0.1+0.1j):
    return z**3 + c/(z**3)
def f4(z, c=0.5+0.3j):
    return z**3 + c/(z**3)
def f5(z, c=0+0.0125j):
    return z**3 + c/(z**3)
def f6(z, c=-0.285+0.125j):
    return z**3 + c/(z**3)
def f7(z, c=0.005+0j):
    return z**3 + c/(z**3)
def Julia(f, zmin, zmax, m, n, tmax=256):
    xs = np.linspace(zmin.real, zmax.real, n)
    ys = np.linspace(zmin.imag, zmax.imag, m)
    X, Y = np.meshgrid(xs, ys)
    Z = X + 1j * Y
    J = np.ones(Z.shape) * tmax
    for t in range(tmax):
        mask = np.abs(Z) <= 2.
        Z[ mask] = f(Z[mask])
        J[-mask] -= 1
    return J
zmin = -1.3 - 1j * 1.3
zmax = 1.3 + 1j * 1.3
J = Julia(f7, zmin, zmax, m=1024, n=1024)
name = 'julia.png'
cmap = cm.jet
plt.imsave(name, J, cmap=cmap, origin='lower')
cmaps = [m for m in plt.cm.datad]
for i, cmap in enumerate(cmaps):
    c = plt.get_cmap(cmap)
    n = 'julia-%d.png'% i
    plt.imsave(n, J, cmap=c, origin='lower')

