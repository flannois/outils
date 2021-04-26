"""
                        beta
                         /\___
                        /     \___  a
                     c /          \___
                      /               \___
                alpha/_____________________\ phi
                                b
"""

from math import acos, pi, sqrt, atan

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

def interieurTriangleHauteur(a, b):
    # Calcul de la hauteur du triangle "intérieur"
    """L'ERREUR EST ICI"""
    # Il faut calculer la hauteur du triangle aligné sur le segment du rayon /!\ Penser aux médiatrices !

def exterieurTriangleHauteur(rayonCercle, hauteurTriangle):
    # Calcul de la hauteur du triangle "extérieur"
    hauteurExterieurTriangle = rayonCercle * 2 - hauteurTriangle
    return hauteurExterieurTriangle

def angleDuBas(b, hauteurExterieurTriangle):
    hauteur = hauteurExterieurTriangle
    largeur = b/2
    angle = atan(hauteur/largeur)
    angle = angle * 180 / pi
    return angle

def angleTotalBas(angle):
    angle = angle * 2
    return angle

def cercleCoupe(aireCercle, angle):
    aireTotale = aireCercle * angle / 360
    return aireTotale


a = 8
b = 13
c = 9

alpha, beta, phi = calculDesAngles(a, b, c)
r = rayonCercle(a, b, c)
aireCercle = aireCercle(r)
hauteurInterieurTriangle = interieurTriangleHauteur(a, b)
hauteurExterieurTriangle = exterieurTriangleHauteur(r, hauteurInterieurTriangle)


angle = angleDuBas(b, hauteurExterieurTriangle)
angle = angleTotalBas(angle)

aireTotale = cercleCoupe(aireCercle, angle)
print(aireTotale)