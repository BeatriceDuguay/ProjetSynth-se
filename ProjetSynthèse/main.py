#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################

from Produit import  *
from Film import  *
from Livre import  *
from Jeu import  *
from Abonne import  *
from Emprunt import  *
from DetailEmprunt import  *

###############################
#####  MESSAGE IMPORTANT  #####
###############################

# Je n'ai pas réussi à faire les tests. En utilisant le debugger, j'ai remarquer que Python ne va pas voir le setter et
# va directement dans le getter.

#############################
#####       TESTS       #####
#############################

# tests de la classe mère Produit

# la propriété __numeroSerie n'est pas respecté
Produit1 = Produit("Livre", "BBBB4822949392", "POO 2", "Français", 1999, "Drame")

if Produit1.NumeroSerie == "":
    print("Erreur")
else:
    print(Produit1)



