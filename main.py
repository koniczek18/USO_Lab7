import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def simpleModel(x,t):
    return t*t

def zadanie1(active):
    if active:
        t = np.linspace(0, 10, 101)