####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Projet synthèse
###  Nom: Béatrice Duguay
###  No étudiant: 1724602
###  No Groupe: 002
###  Description du fichier: Description de la classe DetailsEmprunt
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################

from Produit import *

###################################
#####  MÉTHODE CONSTRUCTEUR  #####
###################################

class DetailsEmprunt:
    """
    Classe DetailsEmprunt
    """
    def __init__(self, p_numeroDetailEmprunt = "", p_produit = Produit, p_quantite_produit = 0):
        """
            Méthode de type Constructeur avec paramètres et valeurs par défaut
            Définition des attributs publics d'un détail d'emprunt
        """
        self.__numeroDetailEmprunt = p_numeroDetailEmprunt
        self.Produit = p_produit
        self.__quantiteProduit = p_quantite_produit

##################################################
####   Propriétés, accesseurs et mutateurs    ####
##################################################

    # propriété __numeroDetailEmprunt
    def _get_numeroDetailEmprunt(self):
        """
            Accesseur de l'attribut privé __numeroDetailEmprunt
        """
        return self.__numeroDetailEmprunt

    def _set_numeroDetailEmprunt(self, p_numero):
        """
            Mutateur de l'attribur privé __numeroDetailEmprunt
        """
        if len(p_numero) == 7 and p_numero[0:3].isalpha() is True and p_numero[4:6].isnumeric() is True:
            self.__numeroDetailEmprunt = p_numero

    NumeroDetailEmprunt = property(_get_numeroDetailEmprunt, _set_numeroDetailEmprunt)

    # propriété __quantiteProduit
    def _get_quantiteProduit(self):
        """
            Accesseur de l'attribut privé __quantiteProduit
        """
        return self.__quantiteProduit

    def _set_quantiteProduit(self, p_qte_produit):
        """
            Mutateur de l'attribur privé __quantiteProduit
        """
        if p_qte_produit >= 0:
            self.__quantiteProduit = p_qte_produit

    QuantiteProduit = property(_get_quantiteProduit, _set_quantiteProduit)

#############################
#####  MÉTHODE MAGIQUE  #####
#############################

    def __str__(self):
        """
            Méthode spéciale d'affichage. À utiliser avec print(objet)
            :return: Chaine à afficher
        """
        chaine =  " "*60+"\n"+"*"*60+"\n\n"
        chaine += "   Numéro du détail de l'emprunt : " + self.NumeroDetailEmprunt + "\n"
        chaine += str(self.Produit) + "\n"
        chaine += "   Quantité de produit : " + str(self.QuantiteProduit ) + "\n"


