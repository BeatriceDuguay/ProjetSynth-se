####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Projet synthèse
###  Nom: Béatrice Duguay
###  No étudiant: 1724602
###  No Groupe: 002
###  Description du fichier: Description de la classe Jeu
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################

from Produit import *

###################################
#####  MÉTHODE CONSTRUCTEUR  #####
###################################

class Jeu (Produit):
    """
    Classe dérivée Jeu de la classe parent Produit
    """
    def __init__(self, p_type_produit = "", p_numero_serie = "", p_titre_produit = "", p_langue_original = "",
                 p_annee_sortie = "",p_genre = "", p_developpeur_jeu = "", p_moteur_jeu = "", p_console_jeu = ""):
        """
            Méthode de type Constructeur avec paramètres et valeurs par défaut
            Définition des attributs publics d'un jeu
        """
        Produit.__init__(self, p_type_produit, p_numero_serie, p_titre_produit, p_langue_original, p_annee_sortie,
                         p_genre)
        self.__developpeurJeu = p_developpeur_jeu
        self.__moteurJeu = p_moteur_jeu
        self.ConsoleJeu = p_console_jeu

##################################################
####   Propriétés, accesseurs et mutateurs    ####
##################################################

    # propriété __developpeurJeu
    def _get_developpeurJeu(self):
        """
            Accesseur de l'attribut privé __developpeurJeu
        """
        return self.__developpeurJeu

    def _set_developpeurJeu(self, p_developpeur):
        """
            Mutateur de l'attribut privé __developpeurJeu
        """
        if len(p_developpeur) <= 50:
             self.__developpeurJeu = p_developpeur

    DeveloppeurJeu = property(_get_developpeurJeu, _set_developpeurJeu)

    # propriété __moteurJeu
    def _get_moteurJeu(self):
        """
            Accesseur de l'attribut privé __moteurJeu
        """
        return self.__moteurJeu
    def _set_moteurJeu(self, p_moteur):
        """
            Mutateur de l'attribut privé __moteurJeu
        """
        if len(p_moteur) <= 50:
             self.__moteurJeu = p_moteur

    MoteurJeu = property(_get_moteurJeu, _set_moteurJeu)

#############################
#####  MÉTHODE MAGIQUE  #####
#############################

    def __str__(self):
        """
            Méthode spéciale d'affichage. À utiliser avec print(objet)
            :return: Chaine à afficher
        """
        chaine = " " * 60 + "\n" + "*" * 60 + "\n\n"
        chaine += Produit().__str__()
        chaine += "   Développeur du jeu : " + self.DeveloppeurJeu + "\n"
        chaine += "   Moteur du jeu : " + str(self.MoteurJeu) + "\n"
        chaine += "   Console  : " + self.ConsoleJeu + "\n"
