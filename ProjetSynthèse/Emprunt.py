####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Projet synthèse
###  Nom: Béatrice Duguay
###  No étudiant: 1724602
###  No Groupe: 002
###  Description du fichier: Description de la classe Emprunt
####################################################################################

#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################

from Abonne import *
import datetime

###################################
#####  MÉTHODE CONSTRUCTEUR  #####
###################################

class Emprunt:
    """
    Classe Emprunt
    """

    def __init__(self, p_numero_emprunt= "", p_date_emprunt= "",p_succurcale= "", p_det_emprunt = [],
                 p_abonne = Abonne):
        """
            Méthode de type Constructeur avec paramètres et valeurs par défaut
            Définition des attributs publics d'un étudiant
        """
        self.__numeroEmprunt = p_numero_emprunt
        self.__dateEmprunt = p_date_emprunt
        self.Succurcale = p_succurcale
        self.Liste_emprunt = p_det_emprunt
        self.Abonne = p_abonne


##################################################
####   Propriétés, accesseurs et mutateurs    ####
##################################################

    # propriété __numeroEmprunt
    def _get_numeroEmprunt(self):
        """
            Accesseur de l'attribut privé __numeroEmprunt
        """
        return self.__numeroEmprunt

    def _set_numeroEmprunt(self, p_numero):
        """
            Mutateur de l'attribur privé __numeroEmprunt
        """
        if len(p_numero) == 7 and p_numero[0:2].isalpha() is True and p_numero[3:6].isnumeric() is True:
            self.__numeroEmprunt = p_numero

    NumeroEmprunt = property(_get_numeroEmprunt, _set_numeroEmprunt)

    # propriété __dateEmprunt
    def _get_dateEmprunt(self):
        """
            Accesseur de l'attribut privé __dateEmprunt
        """
        return self.__dateEmprunt

    def _set_dateEmprunt(self, p_date):
        """
            Mutateur de l'attribur privé __dateEmprunt
        """
        today = datetime.date.today
        if today > p_date:
            self.__dateEmprunt = p_date

    DateEmprunt = property(_get_dateEmprunt, _set_dateEmprunt)


#############################
#####  MÉTHODE MAGIQUE  #####
#############################

    def __str__(self):
        """
            Méthode spéciale d'affichage. À utiliser avec print(objet)
            :return: Chaine à afficher
        """
        chaine = " " * 60 + "\n" + "*" * 60 + "\n\n"
        chaine += "   Numéro de l'emprunt : " + self.NumeroEmprunt + "\n"
        chaine += "   Date de l'emprunt : " + self.DateEmprunt + "\n"
        chaine += "   Succurcale : " + self.Succurcale + "\n"
        chaine += "   Détails de l'emprunt : " + str(self.Liste_emprunt) + "\n"
        chaine += "   Détails de l'abonné : " + str(self.Abonne)
