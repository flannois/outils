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

def triDesValeurs(a,b,c):    
    # Tri des valeurs pour avoir le plus grand côté en bas (0°)
    if a > b and a > c:
        a,b,c = c,a,b
    elif c > b and c > a:
        a,b,c = a,c,b
        return a, b, c

def calculDesAngles(a,b,c):
  
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

def automatisation():
    while True:
        a = randint(1,14)
        b = randint(1,14)
        c = randint(1,14)
        if a+b > c and a+c > b and b+c > a:
            return a,b,c

#----------------Paramètres----------------
largeurFenetre = 800
hauteurFenetre = 800
echelle = 25
vitesse = 50

tailleStylo = 2
turtle.pensize(tailleStylo)

# Automatisation
a,b,c = automatisation()

# Calculs des angles
a, b, c, alpha, beta, phi = calculDesAngles(a, b, c)

# Calcul rayon cercle
r = rayonCercle(a, b, c)

# Grossissement
a = a*echelle
b = b*echelle
c = c*echelle
r = r*echelle

# Centrage
turtle.up()
turtle.goto(-r/2,-r/2)
turtle.down()

# Calcul de l'aire
aireCercle = aireCercle(r)

# Taille fenêtre
turtle.setup(width=largeurFenetre,height=hauteurFenetre)

# Vitesse de dessin
turtle.speed(vitesse)

# Changement couleur
turtle.color("blue")

# Dessin de b
turtle.color("orange")
turtle.write(round(alpha,2))
turtle.color("blue")
turtle.forward(b/2)
turtle.write("b = {}".format(b/echelle))
turtle.forward(b/2)
turtle.left(180-phi)

# Dessin de a
turtle.color("orange")
turtle.write(round(phi,2))
turtle.color("blue")
turtle.forward(a/2)
turtle.write("a = {}".format(a/echelle))
turtle.forward(a/2)
turtle.left(180-beta)

# Dessin de c
turtle.color("orange")
turtle.write(round(beta,2))
turtle.color("blue")
turtle.forward(c/2)
turtle.write("c = {}".format(c/echelle))
turtle.forward(c/2)
turtle.left(180-alpha)

# Angle pour tracer le cercle
turtle.right(beta)

# Tracage du cercle
turtle.color("red")
turtle.circle(r)





#Boucle infini
turtle.mainloop()

