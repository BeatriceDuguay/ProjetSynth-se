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

# importer la boîte de dialogue
import dialogueProduitJeu

# importer la librairie QtWidgets de QtDesigner
from PyQt5 import QtWidgets

# pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# importer la liste liste_detail_emprunts
from MesListes import liste_detail_emprunts

# importer la classe Jeu
from Jeu import  *

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
    objet.label_erreurNumeroDetailEmpruntInexistant.setVisible(False)
    objet.label_erreurNumeroDetailEmpruntInvalide.setVisible(False)
    objet.label_erreurNumeroSerieInvalide.setVisible(False)
    objet.label_erreurNumeroSerieInexistant.setVisible(False)
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

    # ajouter un jeu
    @pyqtSlot()
    def on_pushButton_ajouterJeu_clicked(self):
        """
        Gestionnaire d'événement pour le bouton ajouterJeu
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
                    jeuBiblio = Jeu()
                    jeuBiblio.DeveloppeurJeu = self.lineEdit_developpeurJeu.text()
                    jeuBiblio.MoteurJeu = self.lineEdit_moteurJeu.text()
                    jeuBiblio.ConsoleJeu = self.comboBox_consoleJeu.currentText()

                    # si le développeur du jeu est invalide, afficher un message d'erreur et vider le line edit
                    # de la société de production
                    if jeuBiblio.DeveloppeurJeu == "":
                        self.lineEdit_developpeurJeu.clear()
                        self.label_erreurDeveloppeurJeuInvalide.setVisible(True)

                    # si le moteur du jeu est invalide, afficher un message d'erreur et vider le line edit
                    if jeuBiblio.MoteurJeu == "":
                        self.lineEdit_moteurJeu.clear()
                        self.label_erreurMoteurJeuInvalide.setVisible(True)

                    # si toutes les infos entrées sont valides
                    if produitBiblio.NumeroSerie != "" and detEmpruntBilio.NumeroDetailEmprunt != "" and \
                        jeuBiblio.DeveloppeurJeu != "" and jeuBiblio.MoteurJeu != "":
                        # pour chaque élément de la liste liste_detail_emprunts
                        for elt in liste_detail_emprunts:
                            # si le numéro du détail l'emprunt de la liste est le même que celui entré dans le line edit
                            if elt.NumeroDetailEmprunt == self.lineEdit_numeroDetailEmprunt.text():
                                # si le numéro de série de la liste est le même que celui entré dans le line edit
                                if elt.Produit.NumeroSerie == self.lineEdit_numeroSerieProduit.text():
                                    liste_detail_emprunts.append(jeuBiblio)
                                    break

                        # vider les line edits
                        self.lineEdit_numeroSerieProduit.clear()
                        self.lineEdit_numeroDetailEmprunt.clear()
                        self.lineEdit_moteurJeu.clear()
                        self.lineEdit_developpeurJeu.clear()

        except Exception as ex:
            print("Désolé, quelque chose ne s'est pas bien passé.", ex.args[0])



    # quitter la fenêtre FenetreJeu
    @pyqtSlot()
    def on_pushButton_quitterJeu_clicked(self):
        """
        Gestionnaire d'événement pour le bouton quitterJeu
        """
        self.close()
        print("Bouton quitterJeu OK")

