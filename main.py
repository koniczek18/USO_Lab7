import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def simpleModel(x,t):
    return t*t

def zadanie1(active):
    if active:
        t = np.linspace(0, 10, 201)
        inted=odeint(simpleModel,y0=[0],t=t)
        c=0
        analitic=1/3*np.power(t,3)
        plt.figure('y`=t^2')
        plt.plot(t,inted,label='Odeint')
        plt.plot(t,analitic,label='Analitic')
        plt.legend()
        plt.show()

def model(x,t,k,w,xi):
    x1=x[0]
    x2=x[1]
    ddy=-2*xi*x2/w-np.sqrt(x1)/w+k/np.power(w,2)
    return [x2,ddy]

def zadanie2(active):
    if active:
        k=2
        w=4
        xi=0.25
        t = np.linspace(0, 50, 1001)
        modelInt = odeint(model, y0=[0,0], t=t,args=(k,w,xi))
        plt.figure('Second order model')
        plt.plot(t,modelInt[:,0],label='x1=y')
        plt.plot(t,modelInt[:,1],label='x2=y`')
        plt.legend()
        plt.show()

if __name__ == '__main__':
    zadanie1(True)
    zadanie2(True)