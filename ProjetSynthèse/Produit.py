####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Projet synthèse
###  Nom: Béatrice Duguay
###  No étudiant: 1724602
###  No Groupe: 002
###  Description du fichier: Description de la classe mère Produit
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################


###################################
#####  MÉTHODE CONSTRUCTEUR  #####
###################################

class Produit:
    """
    Classe parent Produit
    """
    def __init__(self, p_type_produit = "",p_numero_serie = "", p_titre_produit = "", p_langue_origine = "",
                 p_annee_sortie = "", p_genre = ""):
        """
            Méthode de type Constructeur avec paramètres et valeurs par défaut
            Définition des attributs publics d'un étudiant
        """
        self.TypeProduit = p_type_produit
        self.__numeroSerie = p_numero_serie
        self.__titreProduit = p_titre_produit
        self.__langueOrigine = p_langue_origine
        self.__anneeSortie = p_annee_sortie
        self.__genre = p_genre

##################################################
####   Propriétés, accesseurs et mutateurs    ####
##################################################

    # propriété __numeroSerie
    def _get_numeroSerie(self):
        """
            Accesseur de l'attribut privé __numeroSerie
        """
        return self.__numeroSerie

    def _set_numeroSerie(self, p_numero_serie):
        """
            Mutateur de l'attribut privé __numeroSerie
        """
        if len(p_numero_serie) == 7 and p_numero_serie[0].isalpha() is True and p_numero_serie[1:6].isnumeric() \
                is True:
            self.__numeroSerie = p_numero_serie

    NumeroSerie = property(_get_numeroSerie, _set_numeroSerie)

    # propriété __titreProduit
    def _get_titreProduit(self):
        """
            Accesseur de l'attribut privé __titreProduit
        """
        return self.__titreProduit

    def _set_titreProduit(self, p_titre):
        """
            Mutateur de l'attribut privé __titreProduit
        """
        if len(p_titre) <= 100:
            self.__titreProduit = p_titre

    TitreProduit = property(_get_titreProduit, _set_titreProduit)

    # propriété __langueOriginal
    def _get_langueOrigine(self):
        """
            Accesseur de l'attribut privé __langueOrigine
        """
        return self.__langueOrigine

    def _set_langueOrigine(self, p_langue):
        """
            Mutateur de l'attribut privé __langueOrigine
        """
        if len(p_langue) <= 25:
            self.__langueOrigine = p_langue

    LangueOrigine = property(_get_langueOrigine, _set_langueOrigine)

    # propriété __anneeSortie
    def _get_anneeSortie(self):
        """
            Accesseur de l'attribut privé __anneeSortie
        """
        return self.__anneeSortie

    def _set_anneeSortie(self, p_annee):
        """
            Mutateur de l'attribut privé __anneeSortie
        """
        if p_annee.isnumeric() and int(p_annee) >= 0:
            self.__anneeSortie = p_annee

    AnneeSortie = property(_get_anneeSortie, _set_anneeSortie)

    # propriété __genre
    def _get_genre(self):
        """
            Accesseur de l'attribut privé __genre
        """
        return self.__genre

    def _set_genre(self, p_genre):
        """
            Mutateur de l'attribut privé __genre
        """
        if len(p_genre) <= 50:
            self.__genre = p_genre

    Genre = property(_get_genre, _set_genre)

#############################
#####  MÉTHODE MAGIQUE  #####
#############################

    def __str__(self):
        """
            Méthode spéciale d'affichage. À utiliser avec print(objet)
            :return: Chaine à afficher
        """
        chaine =  " "*60+"\n"+"*"*60+"\n\n"
        chaine += "   Type de produit : " + self.TypeProduit + "\n"
        chaine += "   Numéro de série : " + self.NumeroSerie + "\n"
        chaine += "   Titre du produit : " + self.TitreProduit + "\n"
        chaine += "   Langue original : " + self.LangueOrigine + "\n"
        chaine += "   Année de sortie/publication : " + self.AnneeSortie + "\n"
        chaine += "   Genre : " + self.Genre + "\n"
        return chaine

