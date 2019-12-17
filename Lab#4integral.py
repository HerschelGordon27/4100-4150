import numpy as np
import math 
import matplotlib.pyplot as plt
from scipy import constants
from scipy.constants import hbar
from scipy.constants import c
from scipy.constants import h
from scipy.constants import k
from scipy.constants import sigma
from scipy.constants import epsilon_0
#T=temperature
h=hbar
s=sigma
T=3000

o=[100,10000,20]
w=np.linspace(10,100,20)


def g(w):
    return (h/(((4*math.pi)**2)*(c**2))) * (w**3)/((math.e**((h*w)/(k*T)))-(1))
q=np.zeros(len(w))  
for i in range(len(w)):
    q[i]=g(w[i])
plt.plot(w,g(w))
plt.show()

T=3000
def f(x):
    return ((x**3)/((math.e**x)-1))*((((math.e**x)-1))*(x**3))

N=50
a=0.00000001
b=1
w=((k**4)*(T**4))/((4*(math.pi**2))*(c**2)*(h**3))
h2=(b-a)/(N)
s= ((1/2)*f(a))+((1/2)*f(b))
for m in range(1,N):
    s += f(a+m*h2)
j=h2*s
print(tol=w*j)

print(uk=T**4)
print(tol/uk)

