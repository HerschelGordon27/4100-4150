import numpy as np
import matplotlib.pyplot as plt
import math
t= np.linspace(0.0,2.0*np.pi,num=50)
x= 2*np.cos(t) + np.cos(2*t)
y= 2*np.sin(t)- np.sin(2*t)
plt.plot(x,y)
plt.show()

w= np.linspace(0.0,10.0*np.pi,num=50)
r= w**2
x2=r*np.cos(w)
y2=r*np.sin(w)
plt.plot(x2,y2)
plt.show()

v= np.linspace(0.0,24.0*np.pi,num=50)
r2= (math.e**(np.cos(v))) + (2*np.cos(4*v))+ ((np.sin(v/12))**5)
x3=r2*np.cos(v)
y3=r2*np.sin(v)
plt.plot(x3,y3)
plt.show()