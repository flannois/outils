"""
                        beta
                         /\___
                        /     \___  a
                     c /          \___
                      /               \___
                alpha/____________________\ phi
                                b
"""

from math import acos, pi, sqrt, atan
import turtle

def calculAngle(a,b,c):
    # Calcul de l'angle en fonction des a, b et c, a étant la longueur en face de l'angle
    angle = acos((a**2 - b**2 - c**2)/(-2*b*c))
    angle = angle * 180 / pi
    return angle

def calculDesAngles(a,b,c):
  # calcul des trois angles (renvoi alpha, beta et phi)
    alpha = calculAngle(a,b,c)
    beta = calculAngle(b,c,a)
    phi = calculAngle(c,a,b)
    return alpha, beta, phi

def rayonCercle(a,b,c):
    # Calcul du rayon du cercle
    s = (a+b+c)/2
    A = sqrt(s*(s-a)*(s-b)*(s-c))
    rayon = (a*b*c)/(4*A)
    return rayon

def aireCercle(rayon):
    # Calcul aire du cercle
    aire = pi * rayon**2
    return aire

echelle = 100
vitesse = 10
marge = 50

a = 4
b = 2
c = 3

alpha, beta, phi = calculDesAngles(a, b, c)

r = rayonCercle(a, b, c)
aireCercle = aireCercle(r)

alpha, beta, phi = calculDesAngles(a,b,c)

# Vitesse de dessin
turtle.speed(vitesse)

# Changement couleur
turtle.color("blue")

# Dessin de b
turtle.forward(b*echelle)
turtle.left(180-phi)
turtle.write(phi)

# Dessin de a
turtle.forward(a*echelle)
turtle.left(180-beta)
turtle.write(beta)

# Dessin de c
turtle.forward(c*echelle)
turtle.left(180-alpha)

# Angle pour tracer le cercle
turtle.right(beta)

# Tracage du cercle
turtle.color("red")
turtle.circle(r*echelle)

#Boucle infini
turtle.mainloop()

