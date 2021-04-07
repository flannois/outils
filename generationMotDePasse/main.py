
from random import randint

def generationMdp(longueur,nombre):
    carac = list()
    for i in range(33,127):
        lettre = chr(i)
        carac.append(lettre)

    for nbPsd in range(nombre):
        mdp = str()
        for i in range(longueur):
            var = randint(0,len(carac)-1)
            var = carac[var]
            mdp = "{}{}".format(mdp, var)

        print(mdp)

generationMdp(longueur=20,nombre=5)