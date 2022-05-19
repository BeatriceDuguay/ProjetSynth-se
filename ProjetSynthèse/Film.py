####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Projet synthèse
###  Nom: Béatrice Duguay
###  No étudiant: 1724602
###  No Groupe: 002
###  Description du fichier: Description de la classe Film
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################

from Produit import Produit

###################################
#####  MÉTHODE CONSTRUCTEUR  #####
###################################

class Film (Produit):
    """
    Classe dérivée Film de la classe parent Produit
    """
    def __init__(self, p_type_produit = "",p_numero_serie = "", p_titre_produit = "", p_langue_original = "",
                 p_annee_sortie = "", p_genre = "", p_societe_production = "", p_nom_realisateur = "",
                 p_prenom_realisateur = "", p_duree_film= ""):
        """
            Méthode de type Constructeur avec paramètres et valeurs par défaut
            Définition des attributs publics d'un film
        """
        Produit.__init__(self, p_type_produit, p_numero_serie, p_titre_produit, p_langue_original,
                         p_annee_sortie, p_genre)
        self.__societeProduction = p_societe_production
        self.__nomRealisateur = p_nom_realisateur
        self.__prenomRealisateur = p_prenom_realisateur
        self.__dureeFilm = p_duree_film



##################################################
####   Propriétés, accesseurs et mutateurs    ####
##################################################

    # propriété __societeProduction
    def _get_societeProduction(self):
        """
            Accesseur de l'attribut privé __societeProduction
        """
        return self.__societeProduction

    def _set_societeProduction(self, p_production):
        """
            Mutateur de l'attribut privé __societeProduction
        """
        if len(p_production) <= 100:
            self.__societeProduction = p_production

    SocieteProduction = property(_get_societeProduction, _set_societeProduction)

    # propriété __nomRealisateur
    def _get_nomRealisateur(self):
        """
            Accesseur de l'attribut privé __nomRealisateur
        """
        return self.__nomRealisateur

    def _set_nomRealisateur(self, p_nom):
        """
            Mutateur de l'attribut privé __nomRealisateur
        """
        if p_nom.isalpha() is True:
            self.__nomRealisateur = p_nom

    NomRealisateur = property(_get_nomRealisateur, _set_nomRealisateur)

    # propriété __prenomRealisateur
    def _get_prenomRealisateur(self):
        """
            Accesseur de l'attribut privé __prenomRealisateur
        """
        return self.__prenomRealisateur

    def _set_prenomRealisateur(self, p_prenom):
        """
            Mutateur de l'attribut privé __prenomRealisateur
        """
        if p_prenom.isalpha() is True:
            self.__prenomRealisateur = p_prenom

    PrenomRealisateur = property(_get_prenomRealisateur, _set_prenomRealisateur)

    # propriété __dureeFilm
    def _get_dureeFilm(self):
        """
            Accesseur de l'attribut privé __dureeFilm
        """
        return self.__dureeFilm

    def _set_dureeFilm(self, p_duree):
        """
            Mutateur de l'attribut privé __dureeFilm
        """
        if p_duree.isnumeric() and int(p_duree) >= 0:
            self.__dureeFilm = p_duree

    DureeFilm = property(_get_dureeFilm, _set_dureeFilm)

#############################
#####  MÉTHODE MAGIQUE  #####
#############################
    def __str__(self):
        """
            Méthode spéciale d'affichage. À utiliser avec print(objet)
            :return: Chaine à afficher
        """
        chaine =  " "*60+"\n"+"*"*60+"\n\n"
        #chaine += Produit().__str__()
        chaine += "   Société de production : " + self.SocieteProduction + "\n\n"
        chaine += "   Nom du réalisateur : " + self.PrenomRealisateur + " " + self.NomRealisateur + "\n\n"
        chaine += "   Durée du film : " + self.DureeFilm + " minutes" + "\n\n"
