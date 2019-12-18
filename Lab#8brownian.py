import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
%matplotlib notebook
from numpy.random import random as rand



L=101
fig = plt.figure(figsize=(2,2))
ax = plt.axes(xlim=(-L/2, L/2), ylim=(-L/2, L/2))
particle= plt.Circle(([], []), 5, fc='b')
n=1000000

x=2*(rand(n)<0.5)-1
y=2*(rand(n)<0.5)-1
xc=x.cumsum()
yc=y.cumsum()
def update(n,a,b,particle):
    particle.center=(a[n],b[n])
    return particle,
part= animation.FuncAnimation(fig, update,fargs=(xc,yc,particle),
init_func=init,frames=360,interval=20,blit=True)
part.save('brownian_particle.mp4')
plt.show()



import numpy as np
import random
import matplotlib.pyplot as plt
N=1000000
d=9.5e5
e=2.718

def montecarlo(f,a,b,N):
    x=np.arange(a,b,0.1)
    y=f(x)
    fm=max(y)
    yr=0+np.random.random(N)*fm
    xr=0+np.random.random(N)*1
    b1 = np.where(yr < f(xr))
    b2 = np.where(yr >= f(xr))
    
    plt.plot(x,y)
    plt.scatter(xr[b1],yr[b1])
    plt.scatter(xr[b2],yr[b2])
    print((fm*1*(len(b1[0]/N)))/d)


def f3(x):
    return (x**-0.5)/((e**x)+1)


montecarlo(f3, 0.01, 1, N)
plt.show()