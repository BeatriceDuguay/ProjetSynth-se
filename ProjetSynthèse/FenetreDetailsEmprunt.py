####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Projet synthèse
###  Nom: Béatrice Duguay
###  No étudiant: 1724602
###  No Groupe: 002
###  Description du fichier: Description de la classe FenetreDetailsEmprunt
####################################################################################

#######################################
###          IMPORTATIONS           ###
#######################################

# pour la réinitialisation de la date dans le dateEdit
from PyQt5.QtCore import QDate

# importer la boîte de dialogue
import dialogueDetailsEmprunt
from FenetreFilm import FenetreFilm
from FenetreJeu import FenetreJeu
from FenetreLivre import FenetreLivre

# importer la librairie QtWidgets de QtDesigner
from PyQt5 import QtWidgets

# pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# importer la classe Produit
from Produit import  *

# importer la classe Film
from Film import  *

# importer la classe Livre
from Livre import  *

# importer la classe Jeu
from Jeu import  *

# importer la classe Abonne
from Abonne import  *

# importer la classe Emprunt
from Emprunt import  *

# importer la classe DetailsEmprunt
from DetailsEmprunt import  *

##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################

# déclarer une liste de détail d'emprunts
liste_detail_emprunts = []

#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

####### CODE UTILISÉ (AVEC MODIFICATIONS) DE: #######
# Exercice 1 - Interface graphique par Hasna Hocini #
#####################################################

# fonction qui permet de s'assurer que l'abonné n'est pas déjà dans la liste des abonnés
def verifier_liste_detail_emprunts(p_numero):
    """
    Vérifier si l'abonné est déjà dans la liste des abonnés
        :param p_numero: le numéro de l'abonné
        :return: Retourner False s'il est dans la liste et retourner True s'il n'est pas dans la liste
    """
    # parcourir la liste des abonnés
    for elt in liste_detail_emprunts:
        if elt.NumeroDetailEmprunt == p_numero.capitalize():
            return False
    return True


####### CODE UTILISÉ (AVEC MODIFICATIONS) DE: #######
# Exercice 1 - Interface graphique par Hasna Hocini #
#####################################################
# fonction qui permet de cacher les messages d'erreur
def cacher_labels_erreur(objet):
    """
    Cacher les différents labels d'erreur
        :param objet:
    """
    objet.label_erreurNumeroDetailEmpruntExiste.setVisible(False)
    objet.label_erreurNumeroDetailEmpruntInvalide.setVisible(False)
    objet.label_erreurQuantiteProduitInvalide.setVisible(False)
    objet.label_erreurNumeroSerieExiste.setVisible(False)
    objet.label_erreurNumeroSerieInvalide.setVisible(False)
    objet.label_erreurTitreProduitInvalide.setVisible(False)
    objet.label_erreurLangueOrigineInvalide.setVisible(False)
    objet.label_erreurAnneeSortieInvalide.setVisible(False)
    objet.label_erreurGenreProduitInvalide.setVisible(False)


#############################################################
######  DÉFINITIONS DE LA CLASSE FenetreDetailsEmprunt  #####
#############################################################

class FenetreDetailsEmprunt(QtWidgets.QDialog, dialogueDetailsEmprunt.Ui_Dialog):

    def __init__(self, parent=None):
        """
        Constructeur de la classe FenetreDetailsEmprunt
        :param parent: QtWidgets.QMainWindow et dialogueDetailsEmprunt.Ui_Dialog
        """
        # appel du constructeur parent
        super(FenetreDetailsEmprunt, self).__init__(parent)
        # préparer l'interface graphique
        self.setupUi(self)
        # change le nom de la fenêtre de dialogue
        self.setWindowTitle("Gestion des détails d'emprunts")
        # appel de la fonction cacher_labels_erreur
        cacher_labels_erreur(self)

    # ouvrir la fenetre fenetreFilm ou fenetreJeu ou fenetreLivre
    @pyqtSlot()
    def on_pushButton_produit_clicked(self):
        """
        Gestionnaire d'événement pour le bouton produit
        """
        # si le comboxbox typeProduit a le texte Film de sélectionné, ouvrir la fenêtre FenetreFilm
        if self.comboBox_typeProduit.currentText() == "Film":
            # instancier la boîte de dialogue FenetreFilm
            dialog = FenetreFilm()
            # afficher la boîte
            dialog.show()
            reply=dialog.exec_()
            print("Bouton produit (Film) OK")
        # si le comboxbox typeProduit a le texte Jeu de sélectionné, ouvrir la fenêtre FenetreJeu
        if self.comboBox_typeProduit.currentText() == "Jeu":
            # instancier la boîte de dialogue FenetreJeu
            dialog = FenetreJeu()
            # afficher la boîte
            dialog.show()
            reply=dialog.exec_()
            print("Bouton produit (Jeu) OK")
        # si le comboxbox typeProduit a le texte Livre de sélectionné, ouvrir la fenêtre FenetreLivre
        if self.comboBox_typeProduit.currentText() == "Livre":
            # instancier la boîte de dialogue FenetreLivre
            dialog = FenetreLivre()
            # afficher la boîte
            dialog.show()
            reply=dialog.exec_()
            print("Bouton produit (Livre) OK")

