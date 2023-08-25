import os

os.chdir(os.path.dirname(__file__))

def lister_fichiers(repertoire):
    liste = []
    for racine, dossiers, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            liste.append(os.path.join(racine, fichier))
    return liste

def lancerTri(listeComplete):
    for chemin in listeComplete:
        try:
            extension = chemin.split('.')[-1]
        except:
            extension = '0Extension'

        if not os.path.exists(extension) and not extension == 'py':
            os.mkdir(extension)

        if not extension == 'py':
            commande = f'move "{chemin}" {extension}'
            print(commande)
            os.system(commande)
                

dossier_a_trier = 'tri'
listeComplete = lister_fichiers(dossier_a_trier)
lancerTri(listeComplete)