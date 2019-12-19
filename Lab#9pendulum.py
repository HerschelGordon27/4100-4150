import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
v=100
g=9.81
l=0.10
a=0.0
b=10.0
N=1000
h=(b-a)/N

initial=179
radians=(initial*math.pi)/(180)


def f(x,t):
    val1= x[0]
    val2=x[1]
    angle=val2
    equation=(-g/l)*(math.sin(val1))
    return np.array([angle,equation],float)
points=np.linspace(a,b,N)
val=[]
x= np.array([radians,0],float)
for t in points:
    val.append(x[0])
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6
plt.plot(points,val)
plt.show()

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
%matplotlib notebook

fig = plt.figure(figsize=(5,5))
ax = plt.axes(xlim=(-1.25, 1.25), ylim=(-1.25, 1.25))
point=plt.Circle((0,0),radius=0.03,facecolor='red')
ax.add_patch(point)
bob = plt.Circle((0, -1), 0.15, fc='b')

def init():
    bob.center = (0, -1)
    ax.add_patch(bob)
    return bob,

def animate(v):
    x=l*np.sin(v)
    y=-l*np.cos(v)
    
    
    bob.center=(x,y)
    return bob,

anim = animation.FuncAnimation(fig, animate,
init_func=init,frames=360,interval=20,blit=True)
anim.save('solar_system.mp4')
plt.show()