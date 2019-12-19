import math
import sys
import matplotlib.pyplot as plt
import numpy as np
e=8.854e-12


print(e)

x = np.linspace(-1.0, 1.0, 100)
y = np.linspace(-1.0, 1.0, 100)
X,Y=np.meshgrid(x,y)
q1=1
q2=-1
mx=5e11
r=np.linspace(0,0.1,100)

def f(q,r):
    
    return  q/(4*(math.pi)*e*r)
z=np.zeros([len(X),len(Y)])

for i in range(0,len(x)):
    f1=x[i]
    for j in range(0,len(y)):
        f2=y[j]
        distance1= math.sqrt(((f1-0.05)**2)+((f2-0)**2))
        distance2=math.sqrt(((f1+0.05)**2)+((f2-0)**2))
        a1=f(q1,distance1)
        a2=f(q2,distance2)
        t=a1+a2
        
        if abs(t)>mx:
            z[i,j]=mx
        else:
            z[i,j]=t
        
plt.plot(z,X)
plt.show()