####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Projet synthèse
###  Nom: Béatrice Duguay
###  No étudiant: 1724602
###  No Groupe: 002
###  Description du fichier: Description de la classe FenetreFilm
####################################################################################

#######################################
###          IMPORTATIONS           ###
#######################################

# importer la boîte de dialogue
import dialogueProduitFilm

# importer la librairie QtWidgets de QtDesigner
from PyQt5 import QtWidgets

# pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# importer la classe Film
from DetailsEmprunt import DetailsEmprunt

from Emprunt import Emprunt
from Film import Film

# importer la liste liste_detail_emprunts
from MesListes import liste_detail_emprunts


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
from Produit import Produit


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
    objet.label_erreurSocieteProductionInvalide.setVisible(False)
    objet.label_erreurDureeFilmInvalide.setVisible(False)
    objet.label_erreurPrenomRealisateurInvalide.setVisible(False)
    objet.label_erreurNomRealisateurInvalide.setVisible(False)

####################################################
######  DÉFINITIONS DE LA CLASSE FenetreFilm  ######
####################################################

class FenetreFilm(QtWidgets.QDialog, dialogueProduitFilm.Ui_Dialog):

    def __init__(self, parent=None):
        """
        Constructeur de la classe FenetreEmprunt
        :param parent: QtWidgets.QMainWindow et dialogueEmprunt.Ui_Dialog
        """
        # appel du constructeur parent
        super(FenetreFilm, self).__init__(parent)
        # préparer l'interface graphique
        self.setupUi(self)
        # change le nom de la fenêtre de dialogue
        self.setWindowTitle("Gestion des emprunts")
        # appel de la fonction cacher_labels_erreur
        cacher_labels_erreur(self)


#################### CODE UTILISÉ: ###################
# Fichier de code : Exercice 1 - Interface graphique #
# Par : Hasna Hocini                                 #
######################################################

    # ajouter un film
    @pyqtSlot()
    def on_pushButton_ajouterFilm_clicked(self):
        """
        Gestionnaire d'événement pour le bouton ajouterFilm
        """
        # gérer les exceptions
        try:
            # instancier un objet DetailEmprunt pour le test
            test_det_emprunt = DetailsEmprunt()
            # instancier l'attribut NumeroDetailEmprunt de la classe DetailsEmprunt
            test_det_emprunt.NumeroDetailEmprunt = self.lineEdit_numeroDetailEmprunt.text()
            # si le NumeroDetailEmprunt est invalide, afficher un message d'erreur
            if test_det_emprunt.NumeroDetailEmprunt == "":
                # vider le line edit numeroDetailEmprunt
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

                # si le numéro du détail de l'emprunt est inexistant, afficher un messade d'erreur
                if trouve == False:
                    # vide le line edit numeroDetailEmprunt
                    self.lineEdit_numeroDetailEmprunt.clear()
                    self.label_erreurNumeroDetailEmpruntInexistant.setVisible(True)

            # instancier un objet Produit pour le test
            test_produit = Produit()
            # instancier l'attribut NumeroSerie de la classe Produit
            test_produit.NumeroSerie = self.lineEdit_numeroSerieProduit.text()
            # si le NumeroSerie est invalide, afficher un message d'erreur
            if test_produit.NumeroSerie == "":
                # vider le line edit numeroSerieProduit
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

                # si le numéro ne se trouve pas dans la liste des détails d'emprunts, afficher un messade d'erreur
                if trouve == False:
                    # vider le line edit numeroSerieProduit
                    self.lineEdit_numeroSerieProduit.clear()
                    self.label_erreurNumeroSerieInexistant.setVisible(True)

                else:
                    # instancier l'attribut NumeroDetailEmprunt de la classe DetailsEmprunt
                    detEmpruntBilio.NumeroDetailEmprunt = self.lineEdit_numeroDetailEmprunt.text()
                    # instancier l'attribut NumeroSerie de la classe Produit
                    produitBiblio.NumeroSerie = self.lineEdit_numeroSerieProduit.text()
                    # instancier les attributs de la classe Film et l'objet Film
                    filmBiblio = Film()
                    filmBiblio.SocieteProduction = self.lineEdit_societeProduction.text().capitalize()
                    filmBiblio.DureeFilm = self.lineEdit_dureeFilm.text()
                    filmBiblio.PrenomRealisateur = self.lineEdit_prenomRealisateur.text().capitalize()
                    filmBiblio.NomRealisateur = self.lineEdit_nomRealisateur.text().capitalize()

                    # si la société de production est invalide, afficher un message d'erreur
                    if filmBiblio.SocieteProduction == "":
                        # vider le line edit de la société de production
                        self.lineEdit_societeProduction.clear()
                        self.label_erreurSocieteProductionInvalide.setVisible(True)

                    # si la durée du film est invalide, afficher un message d'erreur
                    if filmBiblio.DureeFilm == "":
                        # vider le line edit de la durée du film
                        self.lineEdit_dureeFilm.clear()
                        self.label_erreurDureeFilmInvalide.setVisible(True)

                    # si le prénom du réalisateur est invalide, afficher un message d'erreur
                    if filmBiblio.PrenomRealisateur == "":
                        # vider le line edit du prénom du réalisateur
                        self.lineEdit_prenomRealisateur.clear()
                        self.label_erreurPrenomRealisateurInvalide.setVisible(True)

                    # si le nom du réalisateur est invalide, afficher un message d'erreur
                    if filmBiblio.NomRealisateur == "":
                        # vider le line edit du nom du réalisateur
                        self.lineEdit_nomRealisateur.clear()
                        self.label_erreurNomRealisateurInvalide.setVisible(True)

                    # si toutes les infos entrées sont valides
                    if produitBiblio.NumeroSerie != "" and detEmpruntBilio.NumeroDetailEmprunt != "" and \
                        filmBiblio.SocieteProduction != "" and filmBiblio.DureeFilm != "" and\
                        filmBiblio.PrenomRealisateur != "" and filmBiblio.NomRealisateur != "":

                        # pour chaque élément de la liste liste_detail_emprunts
                        for elt in liste_detail_emprunts:
                            # si le numéro du détail l'emprunt de la liste est le même que celui entré dans le
                            # line edit
                            if elt.NumeroDetailEmprunt == self.lineEdit_numeroDetailEmprunt.text():
                                # si le numéro de série de la liste est le même que celui entré dans le line edit
                                if elt.Produit.NumeroSerie == self.lineEdit_numeroSerieProduit.text():
                                    # ajouter l'objet instancié à la liste liste_detail_emprunts
                                    liste_detail_emprunts.append(filmBiblio)
                                    break

                        # vider les line edits
                        self.lineEdit_numeroSerieProduit.clear()
                        self.lineEdit_numeroDetailEmprunt.clear()
                        self.lineEdit_societeProduction.clear()
                        self.lineEdit_dureeFilm.clear()
                        self.lineEdit_prenomRealisateur.clear()
                        self.lineEdit_nomRealisateur.clear()

        except Exception as ex:
            print("Erreur (ajouterFilm) : ", ex.args[0])


    # quitter la fenêtre FenetreFilm
    @pyqtSlot()
    def on_pushButton_quitterFilm_clicked(self):
        """
        Gestionnaire d'événement pour le bouton quitterFilm
        """
        self.close()
        print("Bouton quitterFilm OK")
