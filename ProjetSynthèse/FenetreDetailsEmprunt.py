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
from Emprunt import Emprunt

from FenetreFilm import FenetreFilm
from FenetreJeu import FenetreJeu
from FenetreLivre import FenetreLivre

# importer la librairie QtWidgets de QtDesigner
from PyQt5 import QtWidgets

# pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# importer les listes
from MesListes import liste_abonnes
from MesListes import liste_emprunts
from MesListes import liste_detail_emprunts

# importer la classe DetailsEmprunt
from DetailsEmprunt import  *


##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################

# déclarer une liste de produits
liste_produits = []

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
        if elt.NumeroDetailEmprunt == p_numero:
            return True
    return False

# fonction qui permet de s'assurer que le produit n'est pas déjà dans la liste des produits
def verifier_liste_produits(p_numero_serie):
    """
    Vérifier si le produit est déjà dans la liste des produits
        :param p_numero: le numéro de série
        :return: Retourner False s'il est dans la liste et retourner True s'il n'est pas dans la liste
    """
    # parcourir la liste des abonnés
    for elt in liste_produits:
        if elt.NumeroSerie == p_numero_serie:
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
    objet.label_erreurNumeroDetailEmpruntExiste.setVisible(False)
    objet.label_erreurNumeroDetailEmpruntInvalide.setVisible(False)
    objet.label_erreurNumeroEmpruntInexistant.setVisible(False)
    objet.label_erreurNumeroEmpruntInvalide.setVisible(False)
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


#################### CODE UTILISÉ: ###################
# Fichier de code : Exercice 1 - Interface graphique #
# Par : Hasna Hocini                                 #
######################################################

    # ouvrir la fenetre fenetreFilm ou fenetreJeu ou fenetreLivre
    @pyqtSlot()
    def on_pushButton_produit_clicked(self):
        """
        Gestionnaire d'événement pour le bouton produit
        """
        # gérer les exceptions
        try:
            # instancier un objet Emprunt pour le test
            test_emprunt = Emprunt()
            # instancier l'attribut NumeroEmprunt de la classe Emprunt
            test_emprunt.NumeroEmprunt = self.lineEdit_numeroEmprunt.text()
            # si le numéro de l'emprunt est invalide affichier un message d'erreur
            if test_emprunt.NumeroEmprunt == "":
                 # vider le line edit
                self.lineEdit_numeroEmprunt.clear()
                self.label_erreurNumeroEmpruntInvalide.setVisible(True)
            else:
                trouve = False
                # pour chaque élément dans la liste liste_emprunts
                for elt in liste_emprunts:
                    # si le numéro de l'emprunt est le même que celui du line edit
                    if elt.NumeroEmprunt == self.lineEdit_numeroEmprunt.text():
                        # l'objet instancier Emprunt fait parti de la liste
                        empruntBiblio = elt
                        trouve = True
                        break

                # si l'emprunt ne se trouve pas dans la liste des emprunts, afficher un message d'erreur
                if trouve == False:
                    # vider le line edit numéro emprunt
                    self.lineEdit_numeroEmprunt.clear()
                    self.label_erreurNumeroEmpruntInexistant.setVisible(True)

                else:
                    # instancier l'attribut NumeroEmprunt de la classe Emprunt
                    empruntBiblio.NumeroEmprunt = self.lineEdit_numeroEmprunt.text()
                    # instancier les attributs de la classe detailsEmprunt et l'objet detailsEmprunt
                    detEmpruntBiblio = DetailsEmprunt()
                    detEmpruntBiblio.NumeroDetailEmprunt = self.lineEdit_numeroDetailEmprunt.text()
                    detEmpruntBiblio.QuantiteProduit = self.lineEdit_quantiteProduit.text()
                    # instancier les attributs de la classe Produit et l'objet Produit
                    produitBiblio = Produit()
                    produitBiblio.TypeProduit = self.comboBox_typeProduit.currentText()
                    produitBiblio.NumeroSerie = self.lineEdit_numeroSerieProduit.text()
                    produitBiblio.TitreProduit = self.lineEdit_titreProduit.text()
                    produitBiblio.LangueOrigine = self.lineEdit_langueOrigineProduit.text().capitalize()
                    produitBiblio.AnneeSortie = self.lineEdit_anneeSortieProduit.text()
                    produitBiblio.Genre = self.lineEdit_genreProduit.text().capitalize()

                    # appel de la fonction verifier_liste_detail_emprunts
                    verifier_detail_emprunt = verifier_liste_detail_emprunts(detEmpruntBiblio.NumeroDetailEmprunt)

                    # appel de la fonction verifier_liste_produits
                    verifier_produits = verifier_liste_produits(produitBiblio.NumeroSerie)

                    # si le numéro du détail de l'emprunt existe dans la liste des détails d'emprunts,
                    # afficher un message d'erreur
                    if verifier_detail_emprunt is True and detEmpruntBiblio.NumeroDetailEmprunt != "":
                        # effacer le line edit du numéro
                        self.lineEdit_numeroDetailEmprunt.clear()
                        self.label_erreurNumeroDetailEmpruntExiste.setVisible(True)

                    # si le numéro de série du produit existe dans la liste des produits, afficher un message d'erreur
                    if verifier_produits is True and produitBiblio.NumeroSerie !="":
                        # vider le line edit du numéro de série
                        self.lineEdit_numeroSerieProduit.clear()
                        self.label_erreurNumeroSerieExiste.setVisible(True)

                    # si le numéro du détail l'emprunt est invalide, afficher un message d'erreur
                    if detEmpruntBiblio.NumeroDetailEmprunt == "":
                        # vider le line edit du numéro du détail de l'emprunt
                        self.lineEdit_numeroDetailEmprunt.clear()
                        self.label_erreurNumeroDetailEmpruntInvalide.setVisible(True)

                    # si la quantité de produit est invalide, afficher un message d'erreur
                    if detEmpruntBiblio.QuantiteProduit == "":
                        # vider le line edit de la quantité
                        self.lineEdit_quantiteProduit.clear()
                        self.label_erreurQuantiteProduitInvalide.setVisible(True)

                    # si le numéro de série est invalide, afficher un message d'erreur
                    if produitBiblio.NumeroSerie == "":
                        # vider le line edit du numéro de série
                        self.lineEdit_numeroSerieProduit.clear()
                        self.label_erreurNumeroSerieInvalide.setVisible(True)

                    # si le titre du produit est invalide, afficher un message d'erreur
                    if produitBiblio.TitreProduit == "":
                        # vider le line edit du titre
                        self.lineEdit_titreProduit.clear()
                        self.label_erreurTitreProduitInvalide.setVisible(True)

                    # si la langue d'origine est invalide, afficher un message d'erreur
                    if produitBiblio.LangueOrigine == "":
                        # vider le line edit de la langue d'origine
                        self.lineEdit_langueOrigineProduit.clear()
                        self.label_erreurLangueOrigineInvalide.setVisible(True)

                    # si l'année de sortie est invalide, afficher un message d'erreur
                    if produitBiblio.AnneeSortie == "":
                        # vider le line edit de l'année de sortie
                        self.lineEdit_anneeSortieProduit.clear()
                        self.label_erreurAnneeSortieInvalide.setVisible(True)

                    # si le genre est invalide, afficher un message d'erreur
                    if produitBiblio.Genre == "":
                        # vider le line edit du genre
                        self.lineEdit_genreProduit.clear()
                        self.label_erreurGenreProduitInvalide.setVisible(True)

                    # si toutes les infos entrées sont valides, le détail de l'emprunt n'existe pas dans la liste
                    # du détail d'emprunts et le produit n'existe pas dans la liste des produits
                    if empruntBiblio.NumeroEmprunt != "" and detEmpruntBiblio.NumeroDetailEmprunt != "" and \
                        detEmpruntBiblio.QuantiteProduit != "" and produitBiblio.NumeroSerie != "" and \
                        produitBiblio.TitreProduit != "" and produitBiblio.LangueOrigine != "" and \
                        produitBiblio.AnneeSortie != "" and produitBiblio.Genre != "" and \
                        verifier_detail_emprunt is False and verifier_produits is False:

                        detEmpruntBiblio.Produit = produitBiblio
                        empruntBiblio.ListeDetailsEmprunt = liste_detail_emprunts
                        # pour chaque élément de la liste liste_emprunt
                        for elt in liste_emprunts:
                            # si le numéro de l'emprunt de la liste est le même que celui entré dans le line edit
                            if elt.NumeroEmprunt == self.lineEdit_numeroEmprunt.text():
                                # ajouter le détail d'emprunt à la liste du détail d'emprunts
                                elt.ListeDetailsEmprunt.append(detEmpruntBiblio)

                        # vider les line edits
                        self.lineEdit_numeroEmprunt.clear()
                        self.lineEdit_numeroDetailEmprunt.clear()
                        self.lineEdit_quantiteProduit.clear()
                        self.lineEdit_numeroSerieProduit.clear()
                        self.lineEdit_titreProduit.clear()
                        self.lineEdit_langueOrigineProduit.clear()
                        self.lineEdit_anneeSortieProduit.clear()
                        self.lineEdit_genreProduit.clear()

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

        # afficher un message d'erreur et l'argument
        except Exception as ex:
            print(" Erreur (produit) : ", ex.args[0])

    # quitter la fenetre fenetreDetailsEmprunt
    @pyqtSlot()
    def on_pushButton_quitterDetailsEmprunt_clicked(self):
        """
        Gestionnaire d'événement pour le bouton quitterDetailsEmprunt
        """
        self.close()
        print("Bouton quitterDetailsEmprunt OK")



