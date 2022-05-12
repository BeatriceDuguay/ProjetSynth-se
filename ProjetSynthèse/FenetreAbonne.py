####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Projet synthèse
###  Nom: Béatrice Duguay
###  No étudiant: 1724602
###  No Groupe: 002
###  Description du fichier: Description de la classe FenetreAbonne
####################################################################################

#######################################
###          IMPORTATIONS           ###
#######################################

# pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# pour la réinitialisation de la date dans le dateEdit
from PyQt5.QtCore import QDate

# importer la boîte de dialogue
import dialogueAbonne

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

# déclarer une liste d'abonnés
liste_abonnes = []

#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

####### CODE UTILISÉ (AVEC MODIFICATIONS) DE: #######
# Exercice 1 - Interface graphique par Hasna Hocini #
#####################################################

# fonction qui permet de s'assurer que l'abonné n'est pas déjà dans la liste des abonnés
def verifier_liste_abonnes(p_numero):
    """
    Vérifier si l'abonné est déjà dans la liste des abonnés
        :param p_numero: le numéro de l'abonné
        :return: Retourner True s'il est dans la liste et retourner False s'il n'est pas dans la liste
    """
    # parcourir la liste des abonnés
    for elt in liste_abonnes:
        if elt.NumeroAbonne == p_numero.capitalize():
            return True
    return False


####### CODE UTILISÉ (AVEC MODIFICATIONS) DE: #######
# Exercice 1 - Interface graphique par Hasna Hocini #
#####################################################
# fonction qui permet de cacher les messages d'erreur
def cacher_labels_erreur(objet):
    """
    Cacher les différents labels d'erreur
        :param objet:
    """
    objet.label_erreurNumeroAbonneExiste.setVisible(False)
    objet.label_erreurNumeroAbonneInvalide.setVisible(False)
    objet.label_erreurPrenomInvalide.setVisible(False)
    objet.label_erreurNomInvalide.setVisible(False)
    objet.label_erreurDateNaissInvalide.setVisible(False)

######################################################
######  DÉFINITIONS DE LA CLASSE FenetreAbonne  ######
######################################################
class FenetreAbonne(QtWidgets.QDialog, dialogueAbonne.Ui_Dialog):

    def __init__(self, parent=None):
        """
        Constructeur de la classe FenetreAbonne
        :param parent: QtWidgets.QMainWindow et dialogueAbonne.Ui_Dialog
        """
        # appel du constructeur parent
        super(FenetreAbonne, self).__init__(parent)
        # préparer l'interface graphique
        self.setupUi(self)
        # change le nom de la fenêtre de dialogue
        self.setWindowTitle("Gestion des abonné(es)")
        # appel de la fonction cacher_labels_erreur
        cacher_labels_erreur(self)

####### CODE UTILISÉ (AVEC MODIFICATIONS) DE: #######
# Exercice 1 - Interface graphique par Hasna Hocini #
#####################################################

    # ajouter un abonné à la liste des abonnés
    @pyqtSlot()
    def on_pushButton_ajouterAbonne_clicked(self):
        """
        Gestionnaire d'événement pour le bouton ajouter
        """
        # appel de la fonction cacher_labels_erreur
        cacher_labels_erreur(self)
        # instancier les attributs de la classe Abonne et l'objet Abonne
        abonneBiblio = Abonne()
        abonneBiblio.NumeroAbonne = self.lineEdit_numeroAbonne.text()
        abonneBiblio.PrenomAbonne = self.lineEdit_prenomAbonne.text().capitalize()
        abonneBiblio.NomAbonne = self.lineEdit_nomAbonne.text().capitalize()
        abonneBiblio.DateNaissAbonne = self.dateEdit_dateNaissAbonne.date()
        # appel de la fonction verifier_liste_abonnes
        verifier_abonne = verifier_liste_abonnes(abonneBiblio.NumeroAbonne)

        # si l'abonné se trouve dans la liste des abonnés, rendre le label d'erreur visible
        if verifier_abonne is True:
            # rénitialiser le line edit du numéro de l'abonné
            self.lineEdit_numeroAbonne.clear()
            self.label_erreurNumeroAbonneExiste.setVisible(True)

        # si l'utilisateur a laissé le champs numéro vide, rendre le label d'erreur visible
        if abonneBiblio.NumeroAbonne == "":
            # rénitialiser le line edit du numéro de l'abonné
            self.lineEdit_numeroAbonne.clear()
            self.label_erreurNumeroAbonneInvalide.setVisible(True)

        # si l'utilisateur a laissé le champs prénom vide, rendre le label d'erreur visible
        if abonneBiblio.PrenomAbonne == "":
            # rénitialiser le line edit du numéro de l'abonné
            self.lineEdit_prenomAbonne.clear()
            self.label_erreurPrenomInvalide.setVisible(True)

        # si l'utilisateur a laissé le champs nom vide, rendre le label d'erreur visible
        if abonneBiblio.NomAbonne == "":
            self.lineEdit_nomAbonne.clear()
            self.label_erreurNomInvalide.setVisible(True)

        # si l'utilisateur a laissé le champs date de naissance vide, rendre le label d'erreur visible
        if abonneBiblio.DateNaissAbonne == "":
            self.dateEdit_dateNaissAbonne.setDate(QDate(2000, 1, 1))
            self.label_erreurDateNaissInvalide.setVisible(True)

        if abonneBiblio.NumeroAbonne != "" and abonneBiblio.PrenomAbonne != "" and abonneBiblio.NomAbonne != "" and \
                abonneBiblio.DateNaissAbonne != "" and verifier_abonne is False:
            liste_abonnes.append(abonneBiblio)

            self.textBrowser_detailsAbonne.append(abonneBiblio.__str__())

            self.lineEdit_numeroAbonne.clear()
            self.lineEdit_numeroAbonne.clear()
            self.lineEdit_prenomAbonne.clear()
            self.lineEdit_nomAbonne.clear()
            self.dateEdit_dateNaissAbonne.setDate(QDate(2000, 1, 1))

    # quitter la fenêtre FenetreAbonne
    @pyqtSlot()
    def on_pushButton_quitterAbonne_clicked(self):
        """
        Gestionnaire d'événement pour le bouton quitterAbonne
        """
        self.close()
        print("Bouton quitterAbonne OK")
