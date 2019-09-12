x= float(input("Enter in a fraction of light: "))
y=float(input("Enter in a distance in light years"))
z= y/x
t=z/((1-(x**2))**.5)
print(z)
print(t)