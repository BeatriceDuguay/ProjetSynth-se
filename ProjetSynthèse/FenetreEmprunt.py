####################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Projet synthèse
###  Nom: Béatrice Duguay
###  No étudiant: 1724602
###  No Groupe: 002
###  Description du fichier: Description de la classe FenetreEmprunt
####################################################################################

#######################################
###          IMPORTATIONS           ###
#######################################

# pour la réinitialisation de la date dans le dateEdit
from PyQt5.QtCore import QDate

# importer la boîte de dialogue
import dialogueEmprunt

# importer la boîte de dialogue FenetreDetailsEmprunt
from DetailsEmprunt import DetailsEmprunt
from FenetreDetailsEmprunt import FenetreDetailsEmprunt

# importer la librairie QtWidgets de QtDesigner
from PyQt5 import QtWidgets

# pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# importer la classe Abonne
from Abonne import Abonne

# importer la classe Emprunt
from Emprunt import Emprunt

# importer les listes
from MesListes import liste_abonnes
from MesListes import liste_detail_emprunts
from MesListes import liste_emprunts

# importer la fonction verifier_liste_abonnes
from FenetreAbonne import verifier_liste_abonnes


#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

#################### CODE UTILISÉ: ###################
# Fichier de code : Exercice 1 - Interface graphique #
# Par : Hasna Hocini                                 #
######################################################

# fonction qui permet de s'assurer que l'emprunt n'est pas déjà dans la liste des emprunts
def verifier_liste_emprunts(p_numero_emprunt):
    """
    Vérifier si l'emprunt est déjà dans la liste des empunts
        :param p_numero: le numéro de l'emprunts
        :return: Retourner False s'il est dans la liste et retourner True s'il n'est pas dans la liste
    """
    # parcourir la liste des emprunts
    for elt in liste_emprunts:
        if elt.NumeroEmprunt == p_numero_emprunt:
            return True
    return False


#################### CODE UTILISÉ: ###################
# Fichier de code : Exercice 1 - Interface graphique #
# Par : Hasna Hocini                                 #
######################################################

# fonction qui permet de cacher les messages d'erreur
def cacher_labels_erreur(objet):
    """
    Cacher les différents labels d'erreur
        :param objet:
    """
    objet.label_erreurNumeroAbonneInvalide.setVisible(False)
    objet.label_erreurNumeroAbonneExistePas.setVisible(False)
    objet.label_erreurNumeroEmpruntExiste.setVisible(False)
    objet.label_erreurNumeroEmpruntInexistant.setVisible(False)
    objet.label_erreurNumeroEmpruntInvalide.setVisible(False)
    objet.label_dateEmpruntInvalide.setVisible(False)


######################################################
######  DÉFINITIONS DE LA CLASSE FenetreEmprunt  #####
######################################################

class FenetreEmprunt(QtWidgets.QDialog, dialogueEmprunt.Ui_Dialog):

    def __init__(self, parent=None):
        """
        Constructeur de la classe FenetreEmprunt
        :param parent: QtWidgets.QMainWindow et dialogueEmprunt.Ui_Dialog
        """
        # appel du constructeur parent
        super(FenetreEmprunt, self).__init__(parent)
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

    # ouvrir la fenêtre FenetreDetailsEmprunt
    @pyqtSlot()
    def on_pushButton_detailsEmprunt_clicked(self):
        """
        Gestionnaire d'événement pour le bouton detailsEmprunt
        """
        # gérer les exceptions
        try:
            # vider le text browser
            self.textBrowser_emprunt.clear()
            # instancier un objet Abonne pour le test
            test_abonne = Abonne()
            # instancier l'attribut NumeroAbonne de la classe Abonne
            test_abonne.NumeroAbonne=self.lineEdit_numeroAbonneEmprunt.text()
            # si le numéro de l'abonné est invalide, afficher un message d'erreur
            if test_abonne.NumeroAbonne == "":
                # vider le line edit numeroAbonne
                self.lineEdit_numeroAbonneEmprunt.clear()
                self.label_erreurNumeroAbonneInvalide.setVisible(True)
            else :
                trouve = False
                # pour chaque élément de la liste liste_abonnes
                for elt in liste_abonnes:
                    # si le numéro de l'abonné est le même que celui du line edit
                    if elt.NumeroAbonne == self.lineEdit_numeroAbonneEmprunt.text():
                        # l'objet instancier Abonne fait parti de la liste liste_abonnes
                        abonneBiblio = elt
                        trouve = True
                        break

                # si l'abonné ne se trouve pas dans la liste des abonnés, afficher un messade d'erreur
                if trouve == False:
                    # vider le line edit numeroAbonneEmprunt
                    self.lineEdit_numeroAbonneEmprunt.clear()
                    self.label_erreurNumeroAbonneExistePas.setVisible(True)

                else:
                    # instancier l'attribut NumeroAbonne de la classe Abonne
                    abonneBiblio.NumeroAbonne = self.lineEdit_numeroAbonneEmprunt.text()
                    # instancier les attributs de la classe Emprunt et l'objet Emprunt
                    empruntBiblio = Emprunt()
                    empruntBiblio.NumeroEmprunt = self.lineEdit_numeroEmprunt.text()
                    empruntBiblio.DateEmprunt = self.dateEdit_dateEmprunt.date()
                    empruntBiblio.Succurcale = self.comboBox_succurcaleEmprunt.currentText()
                    empruntBiblio.ListeDetailsEmprunt = liste_detail_emprunts
                    empruntBiblio.Abonne= abonneBiblio

                    # appel de la fonction verifier_liste_abonnes
                    verifier_abonne = verifier_liste_abonnes(abonneBiblio.NumeroAbonne)

                    # si le numéro de l'abonné n'existe pas dans la liste des abonnés, afficher un message d'erreur
                    if verifier_abonne is False and abonneBiblio.NumeroAbonne != "":
                        # vider le line edit du numéro
                        self.lineEdit_numeroAbonneEmprunt.clear()
                        self.label_erreurNumeroAbonneExistePas.setVisible(True)

                    # appel de la fonction verifier_liste_emprunts
                    verifier_emprunt = verifier_liste_emprunts(empruntBiblio.NumeroEmprunt)
                    # si le numéro de l'emprunt existe dans la liste des emprunts, afficher un message d'erreur
                    if verifier_emprunt is True and empruntBiblio.NumeroEmprunt != "":
                        # vider le line edit du numéro
                        self.lineEdit_numeroEmprunt.clear()
                        self.label_erreurNumeroEmpruntExiste.setVisible(True)

                    # si le numéro de l'abonné est invalide, afficher un message d'erreur
                    if abonneBiblio.NumeroAbonne == "":
                        # vider le line edit du numéro
                        self.lineEdit_numeroAbonneEmprunt.clear()
                        self.label_erreurNumeroAbonneInvalide.setVisible(True)

                    # si le numéro de l'emprunt est invalide, afficher un message d'erreur
                    if empruntBiblio.NumeroEmprunt == "":
                        # vider le line edit du numéro
                        self.lineEdit_numeroEmprunt.clear()
                        self.label_erreurNumeroEmpruntInvalide.setVisible(True)

                    # si la date de l'emprunt est invalide, afficher un message d'erreur
                    if empruntBiblio.DateEmprunt == "":
                        self.label_dateEmpruntInvalide.setVisible(True)

                    # si toutes les infos entrées sont valides et l'abonné n'existe pas dans la liste d'abonnés
                    if abonneBiblio.NumeroAbonne != "" and empruntBiblio.NumeroEmprunt != "" and \
                        empruntBiblio.DateEmprunt != "" and verifier_abonne is True and verifier_emprunt is False:

                        # ajouter l'objet instancié à la liste des emprunts
                        abonneBiblio.ListeEmprunts = liste_emprunts
                        # pour chaque élément de la liste liste_abonnes
                        for elt in liste_abonnes:
                            # si le numéro de l'abonné de la liste est le même que celui entré dans le line edit
                            if elt.NumeroAbonne == self.lineEdit_numeroAbonneEmprunt.text():
                                # ajouter l'emprunt à la liste des emprunts
                                elt.ListeEmprunts.append(empruntBiblio)
                                # afficher les infos de l'emprunt et de l'abonné dans le text browser
                                self.textBrowser_emprunt.append(elt.__str__())

                                # vider les line edits
                                self.lineEdit_numeroAbonneEmprunt.clear()
                                self.lineEdit_numeroEmprunt.clear()
                                self.dateEdit_dateEmprunt.setDate(QDate(2000, 1, 1))


                        # instancier la boîte de dialogue FenetreDetailsEmprunt
                        print("Bouton detailsEmprunt OK")
                        dialog = FenetreDetailsEmprunt()
                        print("ok 11")
                        # afficher la boîte
                        dialog.show()
                        reply=dialog.exec_()
                        print("Bouton detailsEmprunt OK")

        # afficher un message d'erreur et l'argument
        except Exception as ex:
            print("Erreur (detailsEmprunt) : ", ex.args[0])


#################### CODE UTILISÉ: ###################
# Fichier de code : Exercice 1 - Interface graphique #
# Par : Hasna Hocini                                 #
######################################################

    # modifier un emprunt
    @pyqtSlot()
    def on_pushButton_modifierEmprunt_clicked(self):
        """
        Gestionnaire d'événement pour le bouton modifierEmprunt
        """
        # gérer les exceptions
        try:
            # vider le text browser
            self.textBrowser_emprunt.clear()
            # appel de la fonction cacher_labels_erreur
            cacher_labels_erreur(self)
            # instancier les attributs de la classe Emprunt et l'objet Emprunt
            empruntBiblio = Emprunt()
            empruntBiblio.Abonne.NumeroAbonne = self.lineEdit_numeroAbonneEmprunt.text()
            empruntBiblio.NumeroEmprunt = self.lineEdit_numeroEmprunt.text()
            empruntBiblio.DateEmprunt = self.dateEdit_dateEmprunt.date()
            empruntBiblio.Succurcale = self.comboBox_succurcaleEmprunt.currentText()
            # appel de la fonction verifier_liste_emprunts
            verifier_num_emprunt = verifier_liste_emprunts(empruntBiblio.NumeroEmprunt)
            verifier_abonne_emprunt = verifier_liste_emprunts(empruntBiblio.Abonne.NumeroAbonne)

            # si le numéro de l'emprunt est valide, mais n'existe pas dans la liste des emprunts, afficher un
            # message d'erreur
            if verifier_num_emprunt is False and empruntBiblio.NumeroEmprunt != "":
                # vider le line edit du numéro de l'emprunt
                self.lineEdit_numeroEmprunt.clear()
                self.label_erreurNumeroEmpruntInexistant.setVisible(True)

            # si le numéro de l'abonné est valide, mais n'existe pas dans la liste des emprunts, afficher un
            # message d'erreur
            if verifier_abonne_emprunt is False and empruntBiblio.Abonne.NumeroAbonne != "":
                # vider le line edit du numéro de l'abonné
                self.lineEdit_numeroAbonneEmprunt.clear()
                self.label_erreurNumeroAbonneExistePas.setVisible(True)

            # si le numéro de l'abonné est invalide, afficher un message d'erreur
            if empruntBiblio.Abonne.NumeroAbonne == "":
                # vider le line edit du numéro
                self.lineEdit_numeroAbonneEmprunt.clear()
                self.label_erreurNumeroAbonneInvalide.setVisible(True)

            # si le numéro de l'emprunt est invalide, afficher un message d'erreur
            if empruntBiblio.NumeroEmprunt == "":
                # vider le line edit du numéro
                self.lineEdit_numeroEmprunt.clear()
                self.label_erreurNumeroEmpruntInvalide.setVisible(True)

            # si la date de l'emprunt est invalide, afficher un message d'erreur
            if empruntBiblio.DateEmprunt == "":
                self.label_dateEmpruntInvalide.setVisible(True)

            # si le numéro de l'abonné, le numéro de l'emprunt, la date de l'emprunt sont valides,l'emprunt existe
            # dans la liste d'emprunts et le numéro de l'abonné existe dans la liste des emprunts
            if empruntBiblio.Abonne.NumeroAbonne != "" and empruntBiblio.NumeroEmprunt != "" \
                and empruntBiblio.DateEmprunt != "" and verifier_num_emprunt is True \
                and verifier_abonne_emprunt is True:
                # pour chaque élément dans la liste liste_emprunts
                for elt in liste_emprunts:
                    # modifier les infos de l'emprunt
                    if elt.Abonne.NumeroAbonne == self.lineEdit_numeroAbonneEmprunt.text():
                        elt.NumeroEmprunt = self.lineEdit_numeroEmprunt.text()
                        elt.DateEmprunt = self.dateEdit_dateEmprunt.date()
                        elt.Succurcale = self.comboBox_succurcaleEmprunt.currentText()

                # vider le text browser
                self.textBrowser_emprunt.clear()
                # afficher les nouvelles informations de l'emprunt dans le text browser
                self.textBrowser_emprunt.append(empruntBiblio.__str__())
                # vider les line edits
                self.lineEdit_numeroAbonneEmprunt.clear()
                self.lineEdit_numeroEmprunt.clear()
                self.dateEdit_dateEmprunt.setDate(QDate(2000, 1, 1))

        # afficher un message d'erreur et l'argument
        except Exception as ex:
            print("Erreur (modifierEmprunt) : ", ex.args[0])


#################### CODE UTILISÉ: ###################
# Fichier de code : Exercice 1 - Interface graphique #
# Par : Hasna Hocini                                 #
######################################################

    # supprimer un emprunt
    @pyqtSlot()
    def on_pushButton_supprimerEmprunt_clicked(self):
        """
        Gestionnaire d'événement pour le bouton supprimerEmprunt
        """
        # gérer les exceptions
        try:
            # vider le text browser
            self.textBrowser_emprunt.clear()
            # appel de la fonction cacher_labels_erreur
            cacher_labels_erreur(self)
            # instancier les attributs de la classe Emprunt et l'objet Emprunt
            empruntBiblio = Emprunt()
            empruntBiblio.Abonne.NumeroAbonne = self.lineEdit_numeroAbonneEmprunt.text()
            empruntBiblio.NumeroEmprunt = self.lineEdit_numeroEmprunt.text()
            empruntBiblio.DateEmprunt = self.dateEdit_dateEmprunt.date()
            empruntBiblio.Succurcale = self.comboBox_succurcaleEmprunt.currentText()
            # appel de la fonction verifier_liste_emprunts
            verifier_emprunt = verifier_liste_emprunts(empruntBiblio.NumeroEmprunt)
            # appel de la fonction verifier_liste_abonnes
            verifier_abonne = verifier_liste_abonnes(empruntBiblio.Abonne.NumeroAbonne)

            # si le numéro de l'abonné, le numéro de l'emprunt, la date de l'emprunt sont valides, l'emprunt existe
            # dans la liste d'emprunts et l'abonne existe dans la liste des abonnés
            if empruntBiblio.Abonne.NumeroAbonne != "" and empruntBiblio.NumeroEmprunt != "" \
                and empruntBiblio.DateEmprunt != "" and verifier_emprunt is True :
                for elt in liste_emprunts:
                    # chercher dans la liste des emprunts un emprunt avec les infos entrées
                    if elt.Abonne.NumeroAbonne == self.lineEdit_numeroAbonneEmprunt.text() \
                        and elt.NumeroEmprunt == self.lineEdit_numeroEmprunt.text() \
                        and elt.DateEmprunt == self.dateEdit_dateEmprunt.date() \
                        and elt.Succurcale == self.comboBox_succurcaleEmprunt.currentText() :
                        # supprimer l'emprunt de la liste liste_emprunts
                        liste_emprunts.remove(elt)
                        # vider le texte browser
                        self.textBrowser_emprunt.clear()
                        # vider les line edits
                        self.lineEdit_numeroAbonneEmprunt.clear()
                        self.lineEdit_numeroEmprunt.clear()
                        self.dateEdit_dateEmprunt.setDate(QDate(2000, 1, 1))
                        break
            # si le numéro de l'abonné, le numéro de l'emprunt, la date de l'emprunt sont valides, mais
            # l'emprunt n'existe pas dans la liste d'emprunts et l'abonné n'existe pas dans la liste d'abonnés,
            # afficher un message d'erreur
            if empruntBiblio.Abonne.NumeroAbonne != "" and empruntBiblio.NumeroEmprunt != "" \
                and empruntBiblio.DateEmprunt != "" and verifier_emprunt is False and verifier_abonne is False:
                # vider le line edit
                self.lineEdit_numeroEmprunt.clear()
                self.label_erreurNumeroEmpruntInexistant.setVisible(True)

            # si le numéro de l'abonné est invalide, afficher un message d'erreur
            if empruntBiblio.Abonne.NumeroAbonne == "":
                # vider le line edit du numéro
                self.lineEdit_numeroAbonneEmprunt.clear()
                self.label_erreurNumeroAbonneInvalide.setVisible(True)

            # si le numéro de l'emprunt est invalide, afficher un message d'erreur
            if empruntBiblio.NumeroEmprunt == "":
                # vider le line edit du numéro
                self.lineEdit_numeroEmprunt.clear()
                self.label_erreurNumeroEmpruntInvalide.setVisible(True)

            # si la date de l'emprunt est invalide, afficher un message d'erreur
            if empruntBiblio.DateEmprunt == "":
                self.label_dateEmpruntInvalide.setVisible(True)

        # afficher un message d'erreur et l'argument
        except Exception as ex:
            print("Erreur (supprimerEmprunt) : ", ex.args[0])


#################### CODE UTILISÉ: ###################
# Fichier de code : Exercice 1 - Interface graphique #
# Par : Hasna Hocini                                 #
######################################################

    # afficher un emprunt
    @pyqtSlot()
    def on_pushButton_afficherEmprunt_clicked(self):
        """
        Gestionnaire d'événement pour le bouton afficherEmprunt
        """
        # gérer les exceptions
        try:
            # vider le text browser
            self.textBrowser_emprunt.clear()
            # appel de la fonction cacher_labels_erreur
            cacher_labels_erreur(self)
            # instancier les attributs de la classe Emprunt et l'objet Emprunt
            empruntBiblio = Emprunt()
            empruntBiblio.Abonne.NumeroAbonne = self.lineEdit_numeroAbonneEmprunt.text()
            empruntBiblio.NumeroEmprunt = self.lineEdit_numeroEmprunt.text()
            empruntBiblio.DateEmprunt = self.dateEdit_dateEmprunt.date()
            empruntBiblio.Succurcale = self.comboBox_succurcaleEmprunt.currentText()
            empruntBiblio.ListeDetailsEmprunt = liste_detail_emprunts

            # appel de la fonction verifier_liste_emprunts
            verifier_emprunt = verifier_liste_emprunts(empruntBiblio.NumeroEmprunt)

            # si le numéro de l'abonné, le numéro de l'emprunt, la date de l'emprunt sont valides
            # et l'emprunt existe dans la liste d'emprunts
            if empruntBiblio.Abonne.NumeroAbonne != "" and empruntBiblio.NumeroEmprunt != "" \
                and empruntBiblio.DateEmprunt != "" and verifier_emprunt is True:
                for elt in liste_emprunts:
                    # chercher dans la liste des emprunts un emprunt avec les infos entrées
                    if elt.Abonne.NumeroAbonne == self.lineEdit_numeroAbonneEmprunt.text() \
                        and elt.NumeroEmprunt == self.lineEdit_numeroEmprunt.text() \
                        and elt.DateEmprunt == self.dateEdit_dateEmprunt.date() \
                        and elt.Succurcale == self.comboBox_succurcaleEmprunt.currentText() :

                        # pour chaque élément de la liste liste_abonnes
                        for elt in liste_abonnes:
                            # si le numéro de l'abonné de la liste est le même que celui entré dans le line edit
                            if elt.NumeroAbonne == self.lineEdit_numeroAbonneEmprunt.text():
                                # afficher les informations de l'emprunt dans le text browser
                                self.textBrowser_emprunt.append(empruntBiblio.__str__())
                                # vider les line edits
                                self.lineEdit_numeroAbonneEmprunt.clear()
                                self.lineEdit_numeroEmprunt.clear()
                                self.dateEdit_dateEmprunt.setDate(QDate(2000, 1, 1))
                                break

            # si le numéro de l'abonné est invalide, afficher un message d'erreur et vider le line edit du numéro
            if empruntBiblio.Abonne.NumeroAbonne == "":
                self.lineEdit_numeroAbonneEmprunt.clear()
                self.label_erreurNumeroAbonneInvalide.setVisible(True)

            # si le numéro de l'emprunt est invalide, afficher un message d'erreur et vider le line edit du numéro
            if empruntBiblio.NumeroEmprunt == "":
                self.lineEdit_numeroEmprunt.clear()
                self.label_erreurNumeroEmpruntInvalide.setVisible(True)

            # si la date de l'emprunt est invalide, afficher un message d'erreur
            if empruntBiblio.DateEmprunt == "":
                self.label_dateEmpruntInvalide.setVisible(True)

        # afficher un message d'erreur et l'argument
        except Exception as ex:
            print("Erreur : (afficherEmprunt) ", ex.args[0])

    # quitter la fenêtre FenetreEmprunt
    @pyqtSlot()
    def on_pushButton_quitterEmprunt_clicked(self):
        """
        Gestionnaire d'événement pour le bouton quitterEmprunt
        """
        self.close()
        print("Bouton quitterEmprunt OK")

