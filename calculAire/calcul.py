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


# Import pour l'automatisation
from random import randint


def calculAngle(a,b,c):
    # Calcul de l'angle en fonction des a, b et c, a étant la longueur en face de l'angle
    angle = acos((a**2 - b**2 - c**2)/(-2*b*c))
    angle = angle * 180 / pi
    return angle

def calculDesAngles(a,b,c):
    # Tri des valeurs pour avoir le plus grand côté en bas (0°)
    if a > b and a > c:
        a,b,c = c,a,b
    elif c > b and c > a:
        a,b,c = a,c,b
    
    # Calcul des trois angles (renvoi a, b, c, alpha, beta et phi)
    alpha = calculAngle(a,b,c)
    beta = calculAngle(b,c,a)
    phi = calculAngle(c,a,b)
    return a, b, c, alpha, beta, phi

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

echelle = 25
vitesse = 50

a = 9
b = 4
c = 6


a, b, c, alpha, beta, phi = calculDesAngles(a, b, c)

r = rayonCercle(a, b, c)
aireCercle = aireCercle(r)


# Vitesse de dessin
turtle.speed(vitesse)

# Changement couleur
turtle.color("blue")

# Dessin de b
turtle.color("orange")
turtle.write(round(alpha,2))
turtle.color("blue")
turtle.forward(b/2*echelle)
turtle.write("b")
turtle.forward(b/2*echelle)
turtle.left(180-phi)

# Dessin de a
turtle.color("orange")
turtle.write(round(phi,2))
turtle.color("blue")
turtle.forward(a/2*echelle)
turtle.write("a")
turtle.forward(a/2*echelle)
turtle.left(180-beta)

# Dessin de c
turtle.color("orange")
turtle.write(round(beta,2))
turtle.color("blue")
turtle.forward(c/2*echelle)
turtle.write("c")
turtle.forward(c/2*echelle)
turtle.left(180-alpha)

# Angle pour tracer le cercle
turtle.right(beta)

# Tracage du cercle
turtle.color("red")
turtle.circle(r*echelle)

# tracage médiatrice "b"
turtle.color("blue")
turtle.left(beta)
turtle.forward(b/2*echelle)
turtle.color("grey")
turtle.right(90)
turtle.forward(r*echelle)



#Boucle infini
turtle.mainloop()

