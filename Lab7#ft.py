import numpy as np
import matplotlib.pyplot as plt
from cmath import exp,pi
import math

B=1000
w=np.linspace(0,1,N)


def dft(y):
    N = len(y)
    c = np.zeros(N,complex)
    for k in range(N):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c


square= np.sin(2 * np.pi * t)
t = np.linspace(0, 1, B, endpoint=False)

plt.plot(t, dft(square))
plt.show()


from scipy import signal
saw= signal.sawtooth(2 * np.pi * 5 * t, width=.5)
plt.plot(t,dft(saw))
plt.show()



w=np.linspace(0,1,B)
def p(w):
    return np.sin(np.pi * w / B) * np.sin(20 * np.pi * w / B)
ymod=np.zeros(len(w))
for j in range(len(w)):
               ymod[j]=p(w[j])
plt.plot(w,dft(p(w)))
plt.show()
