####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Projet synthèse
###  Nom: Béatrice Duguay
###  No étudiant: 1724602
###  No Groupe: 002
###  Description du fichier: Description de la classe FenetreJeu
####################################################################################

#######################################
###          IMPORTATIONS           ###
#######################################

# pour la réinitialisation de la date dans le dateEdit
from PyQt5.QtCore import QDate

# importer la boîte de dialogue
import dialogueProduitJeu

# importer la boîte de dialogue FenetreDetailsEmprunt
import FenetreDetailsEmprunt

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


#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

####### CODE UTILISÉ (AVEC MODIFICATIONS) DE: #######
# Exercice 1 - Interface graphique par Hasna Hocini #
#####################################################

# fonction qui permet de s'assurer que l'abonné n'est pas déjà dans la liste des abonnés
def verifier_liste_emprunts(p_numero):
    """
    Vérifier si l'emprunt est déjà dans la liste des empunts
        :param p_numero: le numéro de l'emprunts
        :return: Retourner False s'il est dans la liste et retourner True s'il n'est pas dans la liste
    """
    # parcourir la liste des abonnés
    # for elt in liste_abonnes:
    #     if elt.NumeroEmprunt == p_numero.capitalize():
    #         return False
    # return True


####### CODE UTILISÉ (AVEC MODIFICATIONS) DE: #######
# Exercice 1 - Interface graphique par Hasna Hocini #
#####################################################

# fonction qui permet de cacher les messages d'erreur
def cacher_labels_erreur(objet):
    """
    Cacher les différents labels d'erreur
        :param objet:
    """
    objet.label_erreurDeveloppeurJeuInvalide.setVisible(False)
    objet.label_erreurMoteurJeuInvalide.setVisible(False)

###################################################
######  DÉFINITIONS DE LA CLASSE FenetreJeu  ######
###################################################

class FenetreJeu(QtWidgets.QDialog, dialogueProduitJeu.Ui_Dialog):

    def __init__(self, parent=None):
        """
        Constructeur de la classe FenetreJeu
        :param parent: QtWidgets.QMainWindow et dialogueProduitJeu.Ui_Dialog
        """
        # appel du constructeur parent
        super(FenetreJeu, self).__init__(parent)
        # préparer l'interface graphique
        self.setupUi(self)
        # change le nom de la fenêtre de dialogue
        self.setWindowTitle("Gestion des emprunts")
        # appel de la fonction cacher_labels_erreur
        cacher_labels_erreur(self)

    # quitter la fenêtre FenetreJeu
    @pyqtSlot()
    def on_pushButton_quitterJeu_clicked(self):
        """
        Gestionnaire d'événement pour le bouton quitterJeu
        """
        self.close()
        print("Bouton quitterJeu OK")
