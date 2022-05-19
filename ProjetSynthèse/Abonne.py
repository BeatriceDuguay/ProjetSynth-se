####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Projet synthèse
###  Nom: Béatrice Duguay
###  No étudiant: 1724602
###  No Groupe: 002
###  Description du fichier: Description de la classe Abonne
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################

# pour le séréalisation et la désérialisation
import json


###################################
#####  MÉTHODE CONSTRUCTEUR  #####
###################################

class Abonne:
    """
    Classe Abonne
    """

    def __init__(self, p_numero_abonne="", p_nom_abonne="", p_prenom_abonne="", p_date_naiss="",
                 p_emprunts=[]):
        """
            Méthode de type Constructeur avec paramètres et valeurs par défaut
            Définition des attributs publics d'un abonne
        """
        self.__numeroAbonne = p_numero_abonne
        self.__nomAbonne = p_nom_abonne
        self.__prenomAbonne = p_prenom_abonne
        self.__dateNaissAbonne = p_date_naiss
        self.ListeEmprunts = p_emprunts

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ##################################################

    # propriété __numeroAbonne
    def _get_numeroAbonne(self):
        """
            Accesseur de l'attribut privé __numeroAbonne
        """
        return self.__numeroAbonne

    def _set_numeroAbonne(self, p_numero):
        """
            Mutateur de l'attribut privé __numeroAbonne
        """
        if len(p_numero) == 7 and p_numero[0:1].isalpha() is True and p_numero[2:6].isnumeric() is True:
            self.__numeroAbonne = p_numero

    NumeroAbonne = property(_get_numeroAbonne, _set_numeroAbonne)

    # propriété __nomAbonne
    def _get_nomAbonne(self):
        """
            Accesseur de l'attribut privé __nomAbonne
        """
        return self.__nomAbonne

    def _set_nomAbonne(self, p_nom):
        """
            Mutateur de l'attribut privé __nomAbonne
        """
        if p_nom.isalpha() is True:
            self.__nomAbonne = p_nom

    NomAbonne = property(_get_nomAbonne, _set_nomAbonne)

    # propriété __prenomAbonne
    def _get_prenomAbonne(self):
        """
            Accesseur de l'attribut privé __prenomAbonne
        """
        return self.__prenomAbonne

    def _set_prenomAbonne(self, p_prenom):
        """
            Mutateur de l'attribut privé __prenomAbonne
        """
        if p_prenom.isalpha() is True:
            self.__prenomAbonne = p_prenom

    PrenomAbonne = property(_get_prenomAbonne, _set_prenomAbonne)

    # propriété __dateNaissAbonne
    def _get_dateNaissAbonne(self):
        """
            Accesseur de l'attribut privé __dateNaissAbonne
        """
        return self.__dateNaissAbonne

    #################### CODE UTILISÉ: ###################
    # Fichier de code : Exercice 1 - Interface graphique #
    # Par : Hasna Hocini                                 #
    ######################################################
    def _set_dateNaissAbonne(self, p_date_naiss):
        """
            Mutateur de l'attribut privé __dateNaissAbonne
        """
        if self.age(p_date_naiss) >= 12:
            self.__dateNaissAbonne = p_date_naiss

    DateNaissAbonne = property(_get_dateNaissAbonne, _set_dateNaissAbonne)

    #############################
    #####  MÉTHODE MAGIQUE  #####
    #############################

    def __str__(self):
        """
            Méthode spéciale d'affichage. À utiliser avec print(objet)
            :return: Chaine à afficher
        """
        chaine = " " * 60 + "\n" + "*" * 60 + "\n\n"
        chaine += "   Numéro de l'abonné(e) : " + self.NumeroAbonne + "\n\n"
        chaine += "   Nom de l'abonné(e) : " + self.PrenomAbonne + " " + self.NomAbonne + "\n\n"
        # chaine += "   Date de naissance de l'abonné(e) : "+str(self.DateNaissAbonne.year())+"-" + \
        #          str(self.DateNaissAbonne.month())+"-"+ str(self.DateNaissAbonne.day()) + "\n"

        for elt in self.ListeEmprunts:
            chaine += elt.__str__()

        return chaine

    #############################
    #####  AUTRES MÉTHODES  #####
    #############################

    #################### CODE UTILISÉ: ###################
    # Fichier de code : Exercice 1 - Interface graphique #
    # Par : Hasna Hocini                                 #
    ######################################################
    def age(self, p_date_naiss):
        """
           Méthode permettant de calculer l'age de l'abonne
           :: return : retourne l'âge de l'abonne
        """
        import datetime
        today = datetime.date.today()
        age = today.year - p_date_naiss.year() - (
                (today.month, today.day) < (p_date_naiss.month(), p_date_naiss.day()))
        return age

    #################### CODE UTILISÉ: ###################
    # Fichier de code : Exercice 1 - Interface graphique #
    # Par : Hasna Hocini                                 #
    ######################################################
    def serialiserAbonne(self, p_fichier):
        """
            Méthode permttant de sérialiser un objet de la classe Abonne
            ::param p_fichier : Le nom du fichier qui contiendra l'objet sérialisé
            :: return : retourne 0 si le fichier est ouvert et les informations y sont écrites,
                       1 s'il y a erreur d'écriture et 2 s'il y a erreur d'ouverture
        """

        self.__dict__["_Abonne__dateNaissAbonne"] = str(self.DateNaissAbonne.year()) + "-" + \
                                                    str(self.DateNaissAbonne.month()) + "-" \
                                                    + str(self.DateNaissAbonne.day())

        try:
            with open(p_fichier, "w") as fichier:
                try:
                    # json.dump(self.__dict__, fichier)
                    json.dump(self.__dict__, fichier)
                    return 0
                except:
                    return 1
        except:
            return 2
