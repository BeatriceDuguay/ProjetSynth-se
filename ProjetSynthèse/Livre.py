####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Projet synthèse
###  Nom: Béatrice Duguay
###  No étudiant: 1724602
###  No Groupe: 002
###  Description du fichier: Description de la classe Livre
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################

from Produit import *
import json

###################################
#####  MÉTHODE CONSTRUCTEUR  #####
###################################

class Livre (Produit):
    """
    Classe dérivée Livre de la classe parent Produit
    """
    def __init__(self, p_type_produit = "", p_numero_serie = "", p_titre_produit = "", p_langue_original = "", p_annee_sortie = 0,
                 p_genre = "", p_maison_edition = "", p_nom_auteur ="", p_prenom_auteur ="", p_nombre_pages =0):
        """
            Méthode de type Constructeur avec paramètres et valeurs par défaut
            Définition des attributs publics d'un étudiant
        """
        Produit.__init__(self, p_type_produit, p_numero_serie, p_titre_produit, p_langue_original, p_annee_sortie, p_genre)
        self.__maisonEdition = p_maison_edition
        self.__nomAuteur = p_nom_auteur
        self.__prenomAuteur = p_prenom_auteur
        self.__nombrePages = p_nombre_pages

##################################################
####   Propriétés, accesseurs et mutateurs    ####
##################################################

    # propriété __maisonEdition
    def _get_maisonEdition(self):
        """
            Accesseur de l'attribut privé __maisonEdition
        """
        return self.__maisonEdition

    def _set_maisonEdition(self, p_maisonEdi):
        """
            Mutateur de l'attribut privé __maisonEdition
        """
        if len(p_maisonEdi) <= 100:
            self.__maisonEdition = p_maisonEdi

    MaisonEdition = property(_get_maisonEdition, _set_maisonEdition)

    # propriété __nomAuteur
    def _get_nomAuteur(self):
        """
            Accesseur de l'attribut privé __nomAuteur
        """
        return self.__nomAuteur
    def _set_nomAuteur(self, p_nom):
        """
            Mutateur de l'attribut privé __nomAuteur
        """
        if len(p_nom) <= 50:
            self.__nomAuteur = p_nom

    NomAuteur = property(_get_nomAuteur, _set_nomAuteur)

    # propriété __prenomAuteur
    def _get_prenomAuteur(self):
        """
            Accesseur de l'attribut privé __prenomAuteur
        """
        return self.__prenomAuteur

    def _set_prenomAuteur(self, p_prenom):
        """
            Mutateur de l'attribut privé
        """
        if len(p_prenom) <= 50:
            self.__prenomAuteur = p_prenom

    PrenomAuteur = property(_get_prenomAuteur, _set_prenomAuteur)

    # propriété __nombrePages
    def _get_nombrePages(self):
        """
            Accesseur de l'attribut privé __nombrePages
        """
        return self.__nombrePages

    def _set_nombrePages(self, p_nb_pages):
        """
            Mutateur de l'attribut privé __nombrePages
        """
        if p_nb_pages >= 0:
            self.__nombrePages = p_nb_pages

    NombrePages = property(_get_nombrePages, _set_nombrePages)

#############################
#####  MÉTHODE MAGIQUE  #####
#############################

    def __str__(self):
        """
            Méthode spéciale d'affichage. À utiliser avec print(objet)
            :return: Chaine à afficher
        """
        chaine =  " "*60+"\n"+"*"*60+"\n\n"
        chaine += Produit
        chaine += "   Maison d'édition : " + self.MaisonEdition + "\n"
        chaine += "   Nom de l'auteur : " + self.PrenomAuteur + " " + self.NomAuteur + "\n"
        chaine += "   Nombre de pages : " + str(self.NombrePages) + "\n"

#############################
#####  AUTRES MÉTHODES  #####
#############################

#################### CODE UTILISÉ: ###################
# Fichier de code : Exercice 1 - Interface graphique #
# Par : Hasna Hocini                                 #
######################################################
    def serialiserLivre(self, p_fichier):
        """
            Méthode permttant de sérialiser un objet de la classe Livre
            ::param p_fichier : Le nom du fichier qui contiendra l'objet sérialisé
            :: return : retourne 0 si le fichier est ouvert et les informations y sont écrites,
                       1 s'il y a erreur d'écriture et 2 s'il y a erreur d'ouverture
        """

        try:
            with open(p_fichier , "w") as fichier:
                try:
                    #json.dump(self.__dict__, fichier)
                    json.dump(self.__dict__,fichier)
                    return 0
                except:
                    return 1
        except:
            return 2

#################### CODE UTILISÉ: ###################
# Fichier de code : Serialisation                    #
# Par : Hasna Hocini                                 #
######################################################
    def deserialiserLivre(self, p_fichier):
        """
            Méthode permttant de désérialiser un objet de la classe Livre
            ::param p_fichier : Le nom du fichier qui contient l'objet sérialisé
        """

        with open(p_fichier , "r") as fichier :
            self.__dict__ = json.load(fichier)
