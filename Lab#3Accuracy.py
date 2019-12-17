import numpy as np
import math 
import matplotlib.pyplot as plt
d=[10**-4,10**-6,10**-8,10**-10,10**-12,10**-14]
da= np.asarray(d)
def f(x):
    return x*(x-1)

def g(h):
    x=1
    return (f(x+h)-f(x))/(h)
y=np.zeros(len(da))
for i in range(len(da)):
               y[i]=g(da[i])
plt.plot(da,g(da))
plt.show()

N=100
k=np.linspace(1,N,N)


def inte(k):
    h=2/N
    x=1-(h*k)
    y=math.sqrt(1-(x**2))
    return h*y
u=np.zeros(len(k))
for b in range(len(k)):
    u[b]=inte(k[b])
    
print(sum(u))


    