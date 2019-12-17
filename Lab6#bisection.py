import numpy as np 
import math
import matplotlib.pyplot as plt 

from scipy import constants
from scipy.constants import hbar
from scipy.constants import epsilon_0
eps=epsilon_0
h=hbar
e=np.linspace(1,19,20)
v=20
w=1.e-9
me=constants.value('electron mass')

megteV=np.linspace(1,19,200)
megt=megteV*1.60218e-19

rvj=20*1.60218e-19

def ya(megt):
    return np.tan(np.sqrt((w**2 *me*megt)/(2*(h**2))))
xa= np.zeros(len(megt))

for i in range(len(megt)):
    xa[i]= ya(megt[i])
	
plt.plot(megteV,ya(megt))
plt.ylim([-5,5])
plt.show()

def yb(megteV):
    return np.sqrt(((v-megteV)/(megteV)))
xb= np.zeros(len(megteV))

for u in range(len(megteV)):
    xb[u]= yb(megteV[u])

def yc(megteV):
    return -(np.sqrt(megteV/(v-megteV)))
xc=np.zeros(len(megteV))

for p in range(len(megt)):
    xc[p]= yc(megteV[p])

plt.plot(megteV,yc(megteV))
plt.plot(megteV,yb(megteV))
plt.plot(megteV,ya(megt))
plt.ylim([-5,5])
plt.legend()
plt.show()



x1=megteV
y3=yc(megteV)
y2=yb(megteV)
y1=ya(megteV)


def eq(t):
    return y1[int(t)]-y2[int(t)]
def eqq(t):
    return y1[int(t)]-y3[int(t)]

acc=0.001
def bisection1(eq,a,b, acc):
    if eq(a)- eq(b)==0:
        print("NO")
    else:
        while (b-a)/2.0>acc:
            mid=(a+b)/2.0
            if eq(mid)==0:
                return (mid)
            elif eq(a)*eq(mid)<0:
                b=mid
            else:
                a=mid
        return mid

def bisection2(eqq,a,b, acc):
    if eqq(a)- eqq(b)==0:
        print("NO")
    else:
        while (b-a)/2.0>acc:
            mid=(a+b)/2.0
            if eqq(mid)==0:
                return (mid)
            elif eqq(a)*eqq(mid)<0:
                b=mid
            else:
                a=mid
        return mid
answer1= bisection1(eq,2.5,4,0.001)
answer2= bisection2(eqq,2.5,4,0.001)
answer3=bisection2(eqq,4.2,5,0.001)
answer4= bisection1(eq,7.5,8.5,0.001)
answer5=bisection1(eq,8.5,10.0,0.001)
answer6=bisection2(eq,8.5,10,0.001)
print(answer1)
print(answer2)
print(answer3)
print(answer4)
print(answer5)
print(answer6)
    









