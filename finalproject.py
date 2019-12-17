import numpy as np
import matplotlib.pyplot as plt
import math
###distance from sun in kilometers
earth_distance=1.496e8
mercury_distance=5.7910e7
moon_distance_earth=3.78e5
venus_distance=1.0821e8
mars_distance=2.2792e8
Gravitational=1.327e11
#######orbital period in seconds
mercury_op=7603200
venus_op=19440000
earth_op=31536000
mars_op=59356800
eccentricity_1=0.017


########inputs
planet=input("Enter the planet analyzed here: ")


if planet in ['Mercury', 'mercury', 'MERCURY']:
    a_transfer= ((mercury_distance)+(earth_distance))/2
    Period_trans= math.sqrt(((4*(math.pi**2))*(a_transfer**3))/(Gravitational))
    time_of_flight= 0.5*(Period_trans)
    time= time_of_flight/86400 ######time in days
    
    veo= ((2*math.pi)*(earth_distance))/(earth_op)####velocity earth's orbit
    vmy=  ((2*math.pi)*(mercury_distance))/(mercury_op)#### velocity mercury orbit
    vperihelion=((2*math.pi)*(a_transfer))*(math.sqrt((((2*a_transfer)/(earth_distance))-1)))#####perihelion
    v_one= vperihelion-veo####change velocity one
    vaphelion=((2*math.pi)*(a_transfer))*(math.sqrt((((2*a_transfer)/(mercury_distance))-1)))######aphelion
    v_two= abs(vmy-vaphelion)#####change velocity two
    eccentricity2=0.206
    p1=5.667e7
    p2=7.0311e7
    
    print(time)
if planet in ['Venus', 'venus', 'VENUS']:
    a_transfer= ((venus_distance)+(earth_distance))/2
    Period_trans= math.sqrt(((4*(math.pi**2))*(a_transfer**3))/(Gravitational))
    time_of_flight= 0.5*(Period_trans)
    time= time_of_flight/86400 
    
    veo= ((2*math.pi)*(earth_distance))/(earth_op)
    v_venus=  ((2*math.pi)*(venus_distance))/(venus_op)
    vperihelion=((2*math.pi)*(a_transfer))*(math.sqrt((((2*a_transfer)/(earth_distance))-1)))
    v_one= vperihelion-veo
    vaphelion=((2*math.pi)*(a_transfer))*(math.sqrt((((2*a_transfer)/(venus_distance))-1)))
    v_two= abs(v_venus-vaphelion)
    eccentricity2=0.007
    p1=1.0741e8
    p2=1.089e8
    print(time)
if planet in ['Mars', 'mars', 'MARS']:
    a_transfer= ((mars_distance)+(earth_distance))/2
    Period_trans= math.sqrt(((4*(math.pi**2))*(a_transfer**3))/(Gravitational))
    time_of_flight= 0.5*(Period_trans)
    time= time_of_flight/86400 
    
    
    veo= ((2*math.pi)*(earth_distance))/(earth_op)
    v_mars=  ((2*math.pi)*(mars_distance))/(mars_op)
    vperihelion=((2*math.pi)*(a_transfer))*(math.sqrt((((2*a_transfer)/(earth_distance))-1)))#####perihelion
    v_one= vperihelion-veo
    vaphelion=((2*math.pi)*(a_transfer))*(math.sqrt((((2*a_transfer)/(mars_distance))-1)))######aphelion
    v_two= abs(v_mars-vaphelion)
    eccentricity2=0.093
    p1=2.064e8
    p2=2.4983e8
    print(time)
    




import random
mass_craft=140000e3
decimal_loss=0.3
mass_final=mass_craft*decimal_loss
N=10000
vex=5010
xran=np.zeros(N)

for i in range(len(xran)):
    xran[i]=random.uniform(mass_final,mass_craft)
    
def f(x):
    return vex *math.log(abs(x))
answer=0.0
for i in range(N):
    answer += f(xran[i])

print(answer)

import numpy as np
theta= np.linspace(0,360,90)

lactus=(p1,p2,90)

def rfromsun(lactus):
    return 