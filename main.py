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
    u=1
    ddy=-2*xi*x2/w-np.sqrt(x1)/w+k/np.power(w,2)*u
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

def feedback(x,t,kp,T,kob,xt,a_min,a_max):
    y=x[0]
    e=xt-y
    ek=e*kp
    u=np.clip(ek,a_min,a_max)
    dy=u*kob/T*np.power(np.e,-t/T)
    return [dy,u]

def feedbackModified(x,t,kp,T,kob,xt):
    y=x[0]
    e=xt-y
    ek=e*kp
    dy=ek*kob/T*np.power(np.e,-t/T)
    return [dy,ek]

def zadanie3(active):
    if active:
        kp=2
        T=2
        kob=4
        t=np.linspace(0,10,201)
        a_min=-0.1
        a_max=0.1
        ans1=odeint(feedback,y0=[0,0],t=t,args=(kp,T,kob,1,a_min,a_max))
        ans2 = odeint(feedback, y0=[0, 0], t=t, args=(kp, T, kob, 2, a_min, a_max))
        ans3 = odeint(feedback, y0=[0, 0], t=t, args=(kp, T, kob, 3, a_min, a_max))
        mod1=odeint(feedbackModified,y0=[0,0],t=t,args=(kp,T,kob,1))
        mod2 = odeint(feedbackModified, y0=[0, 0], t=t, args=(kp, T, kob, 2))
        mod3 = odeint(feedbackModified, y0=[0, 0], t=t, args=(kp, T, kob, 3))
        plt.figure('System with feedback and restraint')
        plt.plot(t,ans1[:,0],label='y when x(t)=1(t)')
        plt.plot(t,ans2[:,0],label='y when x(t)=2*1(t)')
        plt.plot(t, ans3[:, 0], label='y when x(t)=3*1(t)')
        if True:
            plt.plot(t, mod1[:, 0], label='y when x(t)=1(t) no u(t) restriction')
            plt.plot(t, mod2[:, 0], label='y when x(t)=2*1(t) no u(t) restriction')
            plt.plot(t, mod3[:, 0], label='y when x(t)=3*1(t) no u(t) restriction')
        plt.legend()
        plt.show()

def pendulum(x,t,R,m,g,d,A,w):
    x1=x[0]
    x2=x[1]
    J=m*R*R
    tm=A*np.cos(w*t)
    dx2=(tm-d*x2-m*g*R*np.sin(x1))/J
    return [x2,dx2]

def zadanie4(active):
    if active:
        R=10
        m=0.01
        g=10
        d=0.5
        A=1.5
        w=0.65
        t = np.linspace(0, 10, 2001)
        ans=odeint(pendulum,y0=[0,0],t=t,args=(R,m,g,d,A,w))
        plt.figure('Pendulum')
        plt.plot(t,ans[:,0],label='Pendulum position')
        plt.legend()
        plt.show()

if __name__ == '__main__':
    zadanie1(False)
    zadanie2(False)
    zadanie3(False)
    zadanie4(True)