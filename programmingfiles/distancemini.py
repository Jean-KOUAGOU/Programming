from math import *
def distance(t,theta):
	return sqrt(36*t**2*(2-cos(theta))**2+4*(5-3*t*sin(theta))**2)

print(distance(0.48, pi/3))