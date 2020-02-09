import scipy.integrate as spi
import numpy as np
import pylab as pl
 
beta=5*0.05214
gamma=0.04
TS=1.0
ND=170
S0=1-1e-6
I0=1e-6
INPUT = (S0, I0, 0.0)
 
def diff_eqs(INP,t):

    Y=np.zeros((3))
    V = INP
    Y[0] = - beta * V[0] * V[1]
    Y[1] = beta * V[0] * V[1] - gamma * V[1]
    Y[2] = gamma * V[1]
    return Y   
 
t_start = 0.0; t_end = ND; t_inc = TS
t_range = np.arange(t_start, t_end+t_inc, t_inc)
RES = spi.odeint(diff_eqs,INPUT,t_range)
 


pl.plot(RES[:,0], label='Susceptibles')  
pl.plot(RES[:,2], label='Recovereds')  
pl.plot(RES[:,1], label='Infectious')
pl.legend(loc=0)
pl.title('SIR-2019nCoV Model')
pl.xlabel('Time')
pl.ylabel('Proportion')
