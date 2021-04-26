"""
                        beta
                         /\___
                        /     \___  a
                     c /          \___
                      /               \___
                alpha/_____________________\ phi
                                b
"""

from math import acos, pi, sqrt

def calculAngle(a,b,c):
    angle = acos((a**2 - b**2 - c**2)/(-2*b*c))
    angle = angle * 180 / pi
    print(angle)
    return angle

def calculDesAngles(a,b,c):
    alpha = calculAngle(a,b,c)
    beta = calculAngle(b,c,a)
    phi = calculAngle(c,a,b)
    return alpha, beta, phi

def rayonCercle(a,b,c):
    s = (a+b+c)/2
    A = sqrt(s*(s-a)*(s-b)*(s-c))
    rayon = (a*b*c)/(4*A)
    return rayon

a = 4.02
b = 6.01
c = 3.61

alpha, beta, phi = calculDesAngles(a, b, c)

r = rayonCercle(a, b, c)

print(r)
