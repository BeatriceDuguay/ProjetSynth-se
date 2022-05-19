####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Projet synthèse
###  Nom: Béatrice Duguay
###  No étudiant: 1724602
###  No Groupe: 002
###  Description du fichier: Description de la classe FenetreLivre
####################################################################################

#######################################
###          IMPORTATIONS           ###
#######################################

# importer la boîte de dialogue
import DetailsEmprunt
import Livre
import dialogueProduitLivre

# importer la librairie QtWidgets de QtDesigner
from PyQt5 import QtWidgets

# pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot, QDate

# importer la liste liste_detail_emprunts
from MesListes import liste_detail_emprunts

# importer la classe Livre
from Livre import  *

# importer la classe DetailsEmprunt
from DetailsEmprunt import  *


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
    objet.label_erreurNumeroDetailEmpruntInexistant.setVisible(False)
    objet.label_erreurNumeroDetailEmpruntInvalide.setVisible(False)
    objet.label_erreurNumeroSerieInvalide.setVisible(False)
    objet.label_erreurNumeroSerieInexistant.setVisible(False)
    objet.label_erreurMaisonEditionInvalide.setVisible(False)
    objet.label_erreurNombrePagesInvalide.setVisible(False)
    objet.label_erreurPrenomAuteurInvalide.setVisible(False)
    objet.label_erreurNomAuteurInvalide.setVisible(False)

#####################################################
######  DÉFINITIONS DE LA CLASSE FenetreLivre  ######
#####################################################

class FenetreLivre(QtWidgets.QDialog, dialogueProduitLivre.Ui_Dialog):

    def __init__(self, parent=None):
        """
        Constructeur de la classe FenetreEmprunt
        :param parent: QtWidgets.QMainWindow et dialogueEmprunt.Ui_Dialog
        """
        # appel du constructeur parent
        super(FenetreLivre, self).__init__(parent)
        # préparer l'interface graphique
        self.setupUi(self)
        # change le nom de la fenêtre de dialogue
        self.setWindowTitle("Gestion des emprunts")
        # appel de la fonction cacher_labels_erreur
        cacher_labels_erreur(self)

    # ajouter un livre
    @pyqtSlot()
    def on_pushButton_ajouterLivre_clicked(self):
        """
        Gestionnaire d'événement pour le bouton ajouterLivre
        """
        try:
            # instancier un objet DetailEmprunt pour le test
            test_det_emprunt = DetailsEmprunt()
            # instancier l'attribut NumeroDetailEmprunt de la classe DetailsEmprunt
            test_det_emprunt.NumeroDetailEmprunt = self.lineEdit_numeroDetailEmprunt.text()
            # si le NumeroDetailEmprunt est valide
            if test_det_emprunt.NumeroDetailEmprunt == "":
                self.lineEdit_numeroDetailEmprunt.clear()
                self.label_erreurNumeroDetailEmpruntInvalide.setVisible(True)
            else:
                trouve = False
                # pour chaque élément dans la liste liste_detail_emprunts
                for elt in liste_detail_emprunts:
                    # si le numéro du détail de l'emprunt est le même que celui du line edit
                    if elt.NumeroDetailEmprunt == self.lineEdit_numeroDetailEmprunt.text():
                        # l'objet instancier DetailsEmprunt fait parti de la liste
                        detEmpruntBilio = elt
                        trouve = True
                        break

                # si le numéro du détail de l'emprunt est inexistant
                if trouve == False:
                    self.label_erreurNumeroDetailEmpruntInexistant.setVisible(True)

            # instancier un objet Produit pour le test
            test_produit = Produit()
            # instancier l'attribut NumeroSerie de la classe Produit
            test_produit.NumeroSerie = self.lineEdit_numeroSerieProduit.text()
            # si le NumeroSerie est valide
            if test_produit.NumeroSerie == "":
                self.lineEdit_numeroSerieProduit.clear()
                self.label_erreurNumeroSerieInvalide.setVisible(True)
            else:
                trouve = False
                # pour chaque élément dans la liste liste_detail_emprunts
                for elt in liste_detail_emprunts:
                    # si le numéro de série du produit est le même que celui du line edit
                    if elt.Produit.NumeroSerie == self.lineEdit_numeroSerieProduit.text():
                        # l'objet instancier Produit fait parti de la liste
                        produitBiblio = elt
                        trouve = True
                        break

                # si le numéro de série du produit est inexistant
                if trouve == False:
                    self.label_erreurNumeroSerieInexistant.setVisible(True)

                else:
                    # instancier l'attribut NumeroDetailEmprunt de la classe DetailsEmprunt
                    detEmpruntBilio.NumeroDetailEmprunt = self.lineEdit_numeroDetailEmprunt.text()
                    # instancier l'attribut NumeroSerie de la classe Produit
                    produitBiblio.NumeroSerie = self.lineEdit_numeroSerieProduit.text()
                    # instancier les attributs de la classe Jeu et l'objet Jeu
                    livreBiblio = Livre()
                    livreBiblio.MaisonEdition = self.lineEdit_maisonEdition.text()
                    livreBiblio.PrenomAuteur = self.lineEdit_prenomAuteur.text()
                    livreBiblio.NomAuteur = self.lineEdit_nomAuteur.text()
                    livreBiblio.NombrePages = self.lineEdit_nombrePages.text()

                    # si la maison d'édition est invalide, afficher un message d'erreur et vider le line edit
                    if livreBiblio.MaisonEdition == "":
                        self.lineEdit_maisonEdition.clear()
                        self.label_erreurMaisonEditionInvalide.setVisible(True)

                    # si le prénom de l'auteur est invalide, afficher un message d'erreur et vider le line edit
                    if livreBiblio.PrenomAuteur == "":
                        self.lineEdit_prenomAuteur.clear()
                        self.label_erreurPrenomAuteurInvalide.setVisible(True)

                    # si le nom de l'auteur est invalide, afficher un message d'erreur et vider le line edit
                    if livreBiblio.NomAuteur == "":
                        self.lineEdit_nomAuteur.clear()
                        self.label_erreurNomAuteurInvalide.setVisible(True)

                    # si le nombre de pages est invalide, afficher un message d'erreur et vider le line edit
                    if livreBiblio.NombrePages == "":
                        self.lineEdit_nombrePages.clear()
                        self.label_erreurNombrePagesInvalide.setVisible(True)

                    # si toutes les infos entrées sont valides
                    if produitBiblio.NumeroSerie != "" and detEmpruntBilio.NumeroDetailEmprunt != "" \
                        and livreBiblio.MaisonEdition != "" and livreBiblio.PrenomAuteur != "" and \
                        livreBiblio.NomAuteur != "" and livreBiblio.NombrePages != "":
                        # pour chaque élément de la liste liste_detail_emprunts
                        for elt in liste_detail_emprunts:
                            # si le numéro du détail l'emprunt de la liste est le même que celui entré dans
                            # le line edit
                            if elt.NumeroDetailEmprunt == self.lineEdit_numeroDetailEmprunt.text():
                                # si le numéro de série de la liste est le même que celui entré dans le line edit
                                if elt.Produit.NumeroSerie == self.lineEdit_numeroSerieProduit.text():
                                    liste_detail_emprunts.append(livreBiblio)
                                    break

                        # vider les line edits
                        self.lineEdit_numeroSerieProduit.clear()
                        self.lineEdit_numeroDetailEmprunt.clear()
                        self.lineEdit_maisonEdition.clear()
                        self.lineEdit_prenomAuteur.clear()
                        self.lineEdit_nomAuteur.clear()
                        self.lineEdit_nombrePages.clear()

        except Exception as ex:
            print("Désolé, quelque chose ne s'est pas bien passé.", ex.args[0])


#################### CODE UTILISÉ: ###################
# Fichier de code : Exercice 1 - Interface graphique #
# Par : Hasna Hocini                                 #
######################################################

    # séréaliser un livre
    @pyqtSlot()
    def on_pushButton_serealiserLivre_clicked(self):
        """
        Gestionnaire d'événement pour le bouton serealiserLivre
        """
        try:
            # appel de la fonction cacher_labels_erreur
            cacher_labels_erreur(self)

            # instancier un objet DetailEmprunt pour le test
            test_det_emprunt = DetailsEmprunt()
            # instancier l'attribut NumeroDetailEmprunt de la classe DetailsEmprunt
            test_det_emprunt.NumeroDetailEmprunt = self.lineEdit_numeroDetailEmprunt.text()
            # si le NumeroDetailEmprunt est valide
            if test_det_emprunt.NumeroDetailEmprunt == "":
                self.lineEdit_numeroDetailEmprunt.clear()
                self.label_erreurNumeroDetailEmpruntInvalide.setVisible(True)
            else:
                trouve = False
                # pour chaque élément dans la liste liste_detail_emprunts
                for elt in liste_detail_emprunts:
                    # si le numéro du détail de l'emprunt est le même que celui du line edit
                    if elt.NumeroDetailEmprunt == self.lineEdit_numeroDetailEmprunt.text():
                        # l'objet instancier DetailsEmprunt fait parti de la liste
                        detEmpruntBilio = elt
                        trouve = True
                        break

                # si le numéro du détail de l'emprunt est inexistant
                if trouve == False:
                    self.label_erreurNumeroDetailEmpruntInexistant.setVisible(True)
            # instancier un objet Produit pour le test
            test_produit = Produit()
            # instancier l'attribut NumeroSerie de la classe Produit
            test_produit.NumeroSerie = self.lineEdit_numeroSerieProduit.text()
            # si le NumeroSerie est valide
            if test_produit.NumeroSerie == "":
                self.lineEdit_numeroSerieProduit.clear()
                self.label_erreurNumeroSerieInvalide.setVisible(True)
            else:
                trouve = False
                # pour chaque élément dans la liste liste_detail_emprunts
                for elt in liste_detail_emprunts:
                    # si le numéro de série du produit est le même que celui du line edit
                    if elt.Produit.NumeroSerie == self.lineEdit_numeroSerieProduit.text():
                        # l'objet instancier Produit fait parti de la liste
                        trouve = True
                        break

                # si le numéro de série du produit est inexistant
                if trouve == False:
                    self.label_erreurNumeroSerieInexistant.setVisible(True)

                else:
                    # instancier l'attribut NumeroDetailEmprunt de la classe DetailsEmprunt
                    detEmpruntBilio.NumeroDetailEmprunt = self.lineEdit_numeroDetailEmprunt.text()
                    # instancier l'attribut NumeroSerie de la classe Produit

                    # instancier les attributs de la classe Abonne et l'objet Abonne
                    livreBiblio = Livre()
                    livreBiblio.NumeroSerie = self.lineEdit_numeroSerieProduit.text()
                    livreBiblio.MaisonEdition = self.lineEdit_maisonEdition.text()
                    livreBiblio.PrenomAuteur = self.lineEdit_prenomAuteur.text()
                    livreBiblio.NomAuteur = self.lineEdit_nomAuteur.text()
                    livreBiblio.NombrePages = self.lineEdit_nombrePages.text()

                    # si toutes les infos entrées sont valides
                    if livreBiblio.NumeroSerie !="" and livreBiblio.MaisonEdition != "" and \
                        livreBiblio.PrenomAuteur != "" and livreBiblio.NomAuteur != "" and \
                        livreBiblio.NombrePages != "":
                        for elt in liste_detail_emprunts:
                            if elt.Produit.NumeroSerie == self.lineEdit_numeroSerieProduit.text():
                                elt = livreBiblio
                                # séréaliser l'objet
                                resultat = elt.serialiserLivre("." + "/" + "Serealiser livres" + "/" +
                                                                       elt.NumeroSerie + "_" +
                                                                       elt.TitreProduit + "_" + ".json")

                                # si la séréalisation fonctionne
                                if resultat == 0:
                                    # vider les line edit
                                    self.lineEdit_numeroSerieProduit.clear()
                                    self.lineEdit_numeroDetailEmprunt.clear()
                                    self.lineEdit_maisonEdition.clear()
                                    self.lineEdit_prenomAuteur.clear()
                                    self.lineEdit_nomAuteur.clear()
                                    self.lineEdit_nombrePages.clear()
                                # sinon afficher des messages d'erreur
                                elif resultat == 1:
                                    # Afficher le message d'erreur d'écriture dans le fichier
                                    self.label_erreurFichierLivre.setText\
                                    ("<font color=\"#aa0000\">Erreur d'écriture dans le fichier</font>")
                                else:
                                    # Afficher le message d'erreur d'ouverture du fichier
                                    self.label_erreurFichierLivre.setText\
                                        ("<font color=\"#aa0000\">Erreur d'ouverture du fichier</font>")

                    # si la maison d'édition est invalide, afficher un message d'erreur et vider le line edit
                    if livreBiblio.MaisonEdition == "":
                        self.lineEdit_maisonEdition.clear()
                        self.label_erreurMaisonEditionInvalide.setVisible(True)

                    # si le prénom de l'auteur est invalide, afficher un message d'erreur et vider le line edit
                    if livreBiblio.PrenomAuteur == "":
                        self.lineEdit_prenomAuteur.clear()
                        self.label_erreurPrenomAuteurInvalide.setVisible(True)

                    # si le nom de l'auteur est invalide, afficher un message d'erreur et vider le line edit
                    if livreBiblio.NomAuteur == "":
                        self.lineEdit_nomAuteur.clear()
                        self.label_erreurNomAuteurInvalide.setVisible(True)

                    # si le nombre de pages est invalide, afficher un message d'erreur et vider le line edit
                    if livreBiblio.NombrePages == "":
                        self.lineEdit_nombrePages.clear()
                        self.label_erreurNombrePagesInvalide.setVisible(True)

        except Exception as ex:
            print("Blabla", ex.args[0])


#################### CODE UTILISÉ: ###################
# Fichier de code : Exercice 1 - Interface graphique #
# Par : Hasna Hocini                                 #
######################################################

    # désérialiser la liste des abonnés
    @pyqtSlot()
    def on_pushButton_deserialiserAbonne_clicked(self):
        """
        Gestionnaire d'événement pour le bouton deserialiserAbonne
        """
        # création d'une chaine vide
        # chaine = ""
        # # pour chaque abonné dans la liste des abonnés
        # for elt in liste_abonnes:
        #     # ajouter les abonnés à la chaine
        #     chaine += elt.__str__()
        # try:
        #     with open("." + "/" + "listeAbonnes"+"/"+"ListeAbonnes.txt", "w") as fichier:
        #         try :
        #             fichier.write(chaine)
        #
        #         except :
        #             self.textBrowser_detailsAbonne.setText("Erreur d'écriture")
        # except :
        #     self.textBrowser_detailsAbonne.setText("Erreur d'ouverture")



    # quitter la fenêtre FenetreLivre
    @pyqtSlot()
    def on_pushButton_quitterLivre_clicked(self):
        """
        Gestionnaire d'événement pour le bouton quitterLivre
        """
        self.close()
        print("Bouton quitterLivre OK")
