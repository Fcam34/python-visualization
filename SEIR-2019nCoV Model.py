import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt


beta = 5*0.05214

gamma_1 = 0

gamma_2 = 0.04

alpha = 1

die = 0.02079

I_0 = 1e-6

E_0 = I_0 * 41

R_0 = 0

S_0 = 1 - I_0 - E_0 - R_0

D_0 = 0

T = 150

INI = (S_0,I_0,E_0,R_0,D_0)


def funcSI(prop,_):
    Y = np.zeros(5)
    X = prop
    
    Y[0] = - beta * X[0] * X[1]
    
    Y[1] = alpha * X[2] - gamma_2 * X[1] - die * X[1]
    
    Y[2] = beta * X[0] * X[1] - (alpha + gamma_1) * X[2]
   
    Y[3] = gamma_1 * X[2] + gamma_2 * X[1]
    
    Y[4] = die * X[1]
    return Y

T_range = np.arange(0,T + 1)

RES = spi.odeint(funcSI,INI,T_range)


plt.plot(RES[:,0],color = 'darkblue',label = 'Susceptible')
plt.plot(RES[:,1],color = 'red',label = 'Infection')
plt.plot(RES[:,2],color = 'orange',label = 'Enfective')
plt.plot(RES[:,3],color = 'green',label = 'Recovery')
plt.plot(RES[:,4],color = 'black',label = 'Die')
plt.title('SEIR-2019nCoV Model')
plt.legend()
plt.xlabel('Day')
plt.ylabel('Proportion')
plt.show()
