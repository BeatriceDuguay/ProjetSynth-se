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
import Abonne
from Abonne import *

###################################
#####  MÉTHODE CONSTRUCTEUR  ######
###################################

class Emprunt:
    """
    Classe Emprunt
    """

    def __init__(self, p_numero_emprunt= "", p_date_emprunt= "",p_succurcale= "", p_det_emprunt = [],
                 p_abonne = Abonne()):
        """
            Méthode de type Constructeur avec paramètres et valeurs par défaut
            Définition des attributs publics d'un étudiant
        """
        self.__numeroEmprunt = p_numero_emprunt
        self.__dateEmprunt = p_date_emprunt
        self.Succurcale = p_succurcale
        self.ListeDetailsEmprunt = p_det_emprunt
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
        if self.date(p_date) >= 0 :
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
        chaine += "   Numéro de l'emprunt : " + self.NumeroEmprunt + "\n\n"
        # chaine += "   Date de l'emprunt : "+str(self.DateEmprunt.year())+"-" + \
        #          str(self.DateEmprunt.month())+"-"+ str(self.DateEmprunt.day()) + "\n\n"
        chaine += "   Succurcale : " + self.Succurcale + "\n\n"

        for elt in self.ListeDetailsEmprunt :
            chaine += elt.__str__()

        return chaine

#############################
#####  AUTRES MÉTHODES  #####
#############################

#################### CODE UTILISÉ: ###################
# Fichier de code : Exercice 1 - Interface graphique #
# Par : Hasna Hocini                                 #
######################################################
    def date(self, p_date_emp):
        """
           Méthode permettant de calculer l'age de l'emprunt
           :: return : retourne l'âge de l'emprunt
        """
        import datetime
        today = datetime.date.today()
        date = today.year - p_date_emp.year() - (
                (today.month, today.day) < (p_date_emp.month(), p_date_emp.day()))
        return date
