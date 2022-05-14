
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

# pour la réinitialisation de la date dans le dateEdit
from PyQt5.QtCore import QDate

# importer la boîte de dialogue
import dialogueAbonne

# importer la librairie QtWidgets de QtDesigner
from PyQt5 import QtWidgets

# pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# importer la classe Abonne
import Abonne

# importer la classe Emprunt
from Emprunt import  *


##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################

# déclarer une liste d'abonnés
liste_abonnes = []
# déclarer une liste d'emprunts
liste_emprunt = []


#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

#################### CODE UTILISÉ: ###################
# Fichier de code : Exercice 1 - Interface graphique #
# Par : Hasna Hocini                                 #
######################################################

# fonction qui permet de s'assurer que l'abonné n'est pas déjà dans la liste des abonnés
def verifier_liste_abonnes(p_numero):
    """
    Vérifier si l'abonné est déjà dans la liste des abonnés
        :param p_numero: le numéro de l'abonné
        :return: Retourner True s'il est dans la liste et retourner False s'il n'est pas dans la liste
    """
    # parcourir la liste des abonnés
    for elt in liste_abonnes:
        if elt.NumeroAbonne == p_numero:
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
    objet.label_erreurNumeroAbonneExiste.setVisible(False)
    objet.label_erreurNumeroAbonneInexistant.setVisible(False)
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


#################### CODE UTILISÉ: ###################
# Fichier de code : Exercice 1 - Interface graphique #
# Par : Hasna Hocini                                 #
######################################################

    # ajouter un abonné à la liste des abonnés
    @pyqtSlot()
    def on_pushButton_ajouterAbonne_clicked(self):
        """
        Gestionnaire d'événement pour le bouton ajouter
        """
        # vider le text browser
        self.textBrowser_detailsAbonne.clear()
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

        # si le numéro de l'abonné existe déjà dans la liste des abonnés, afficher un message d'erreur
        if verifier_abonne is True:
            # effacer le line edit du numéro
            self.lineEdit_numeroAbonne.clear()
            self.label_erreurNumeroAbonneInvalide.setVisible(True)

        # si le numéro de l'abonné est invalide, afficher un message d'erreur et vider le line edit du numéro
        if abonneBiblio.NumeroAbonne == "":
            self.lineEdit_numeroAbonne.clear()
            self.label_erreurNumeroAbonneInvalide.setVisible(True)

        # si le prenom de l'abonné est invalide, afficher un message d'erreur et vider le line edit du prenom
        if abonneBiblio.PrenomAbonne == "":
            self.lineEdit_prenomAbonne.clear()
            self.label_erreurPrenomInvalide.setVisible(True)

        # si le nom de l'abonné est invalide, afficher un message d'erreur et vider le line edit du nom
        if abonneBiblio.NomAbonne == "":
            self.lineEdit_nomAbonne.clear()
            self.label_erreurNomInvalide.setVisible(True)

        # si la date de naissance de l'abonné est invalide, afficher un message d'erreur
        if abonneBiblio.DateNaissAbonne == "":
            self.label_erreurDateNaissInvalide.setVisible(True)

        # si toutes les infos entrées sont valides et l'abonné n'existe pas dans la liste d'abonnés
        if abonneBiblio.NumeroAbonne != "" and abonneBiblio.PrenomAbonne != "" and abonneBiblio.NomAbonne != "" and \
            abonneBiblio.DateNaissAbonne != "" and verifier_abonne is False:
            # ajouter l'abonné à la liste d'abonnés
            liste_abonnes.append(abonneBiblio)
            # afficher les infos de l'abonné dans le text browser
            self.textBrowser_detailsAbonne.append(abonneBiblio.__str__())
            # vider les line edits
            self.lineEdit_numeroAbonne.clear()
            self.lineEdit_prenomAbonne.clear()
            self.lineEdit_nomAbonne.clear()
            self.dateEdit_dateNaissAbonne.setDate(QDate(2000, 1, 1))


#################### CODE UTILISÉ: ###################
# Fichier de code : Exercice 1 - Interface graphique #
# Par : Hasna Hocini                                 #
######################################################

    # modifier un abonné
    @pyqtSlot()
    def on_pushButton_modifierAbonne_clicked(self):
        """
        Gestionnaire d'événement pour le bouton modifierAbonne
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

        # si le numéro de l'abonné est valide, mais n'existe pas dans la liste des abonnés, afficher un message d'erreur
        if verifier_abonne is False and abonneBiblio.NumeroAbonne != "":
            # effacer le line edit du numéro
            self.lineEdit_numeroAbonne.clear()
            self.label_erreurNumeroAbonneInexistant.setVisible(True)

        # si le numéro de l'abonné est invalide, afficher un message d'erreur et vider le line edit du numéro
        if abonneBiblio.NumeroAbonne == "":
            self.lineEdit_numeroAbonne.clear()
            self.label_erreurNumeroAbonneInvalide.setVisible(True)

        # si le prenom de l'abonné est invalide, afficher un message d'erreur et vider le line edit du prenom
        if abonneBiblio.PrenomAbonne == "":
            self.lineEdit_prenomAbonne.clear()
            self.label_erreurPrenomInvalide.setVisible(True)

        # si le prenom de l'abonné est invalide, afficher un message d'erreur et vider le line edit du prenom
        if abonneBiblio.NomAbonne == "":
            self.lineEdit_nomAbonne.clear()
            self.label_erreurNomInvalide.setVisible(True)

        # si la date de naissance de l'abonné est invalide, afficher un message d'erreur
        if abonneBiblio.DateNaissAbonne == "":
            self.label_erreurDateNaissInvalide.setVisible(True)

        # si toutes les infos entrées sont valides et l'abonné existe dans la liste d'abonnés
        if abonneBiblio.NumeroAbonne != "" and abonneBiblio.PrenomAbonne != "" and abonneBiblio.NomAbonne != "" and\
            abonneBiblio.DateNaissAbonne != "" and verifier_abonne is True:
            # modifier les infos de l'abonné (prénom, nom et date de naissance)
            for elt in liste_abonnes:
                # chercher dans la liste d'abonnés le numéro d'abonné entré et modifier les infos de l'abonné
                if elt.NumeroAbonne == self.lineEdit_numeroAbonne.text():
                    elt.PrenomAbonne = self.lineEdit_prenomAbonne.text().capitalize()
                    elt.NomAbonne = self.lineEdit_nomAbonne.text().capitalize()
                    elt.DateNaissAbonne = self.dateEdit_dateNaissAbonne.date()

            # vider le text browser
            self.textBrowser_detailsAbonne.clear()
            # afficher les nouvelles informations de l'abonné dans le text browser
            self.textBrowser_detailsAbonne.append(abonneBiblio.__str__())
            # vider les line edits
            self.lineEdit_numeroAbonne.clear()
            self.lineEdit_prenomAbonne.clear()
            self.lineEdit_nomAbonne.clear()
            self.dateEdit_dateNaissAbonne.setDate(QDate(2000, 1, 1))


#################### CODE UTILISÉ: ###################
# Fichier de code : Exercice 1 - Interface graphique #
# Par : Hasna Hocini                                 #
######################################################

    # supprimer un abonné
    @pyqtSlot()
    def on_pushButton_supprimerAbonne_clicked(self):
        """
        Gestionnaire d'événement pour le bouton supprimerAbonne
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

        # si le numéro, le prénom, le nom et la date de naissance de l'abonné sont valides et l'abonné existe dans la
        # liste d'abonnés
        if abonneBiblio.NumeroAbonne != "" and abonneBiblio.PrenomAbonne != "" and abonneBiblio.NomAbonne != "" and \
                abonneBiblio.DateNaissAbonne != "" and verifier_abonne is True:
            for elt in liste_abonnes:
                # chercher dans la liste des abonnés un abonné avec les infos entrées
                if elt.NumeroAbonne == self.lineEdit_numeroAbonne.text() \
                        and elt.PrenomAbonne == self.lineEdit_prenomAbonne.text().capitalize() \
                        and elt.NomAbonne == self.lineEdit_nomAbonne.text().capitalize() \
                        and elt.DateNaissAbonne == self.dateEdit_dateNaissAbonne.date():
                    liste_abonnes.remove(elt)
                    # vider le texte browser
                    self.textBrowser_detailsAbonne.clear()
                    # vider les line edits
                    self.lineEdit_numeroAbonne.clear()
                    self.lineEdit_prenomAbonne.clear()
                    self.lineEdit_nomAbonne.clear()
                    self.dateEdit_dateNaissAbonne.setDate(QDate(2000,1,1))
                    break

        # si l'abonné ne se trouve pas dans la liste d'abonnés, afficher un message d'erreur
        if abonneBiblio.NumeroAbonne != "" and abonneBiblio.PrenomAbonne != "" and abonneBiblio.NomAbonne != "" and \
                abonneBiblio.DateNaissAbonne != "" and verifier_abonne is False:
            self.label_erreurNumeroAbonneInexistant.setVisible(True)

        # si le numéro de l'abonné est invalide, afficher un message d'erreur et vider le line edit du numéro
        if abonneBiblio.NumeroAbonne == "":
            self.lineEdit_numeroAbonne.clear()
            self.label_erreurNumeroAbonneInvalide.setVisible(True)

        # si le prenom de l'abonné est invalide, afficher un message d'erreur et vider le line edit du prenom
        if abonneBiblio.PrenomAbonne == "":
            self.lineEdit_prenomAbonne.clear()
            self.label_erreurPrenomInvalide.setVisible(True)

        # si le prenom de l'abonné est invalide, afficher un message d'erreur et vider le line edit du prenom
        if abonneBiblio.NomAbonne == "":
            self.lineEdit_nomAbonne.clear()
            self.label_erreurNomInvalide.setVisible(True)

        # si la date de naissance de l'abonné est invalide, afficher un message d'erreur
        if abonneBiblio.DateNaissAbonne == "":
            self.label_erreurDateNaissInvalide.setVisible(True)


    # afficher les abonnés
    @pyqtSlot()
    def on_pushButton_afficherAbonne_clicked(self):
        """
        Gestionnaire d'événement pour le bouton afficherAbonne
        """
        # afficher tous les abonnés de la liste dans le text browser
        for elt in liste_abonnes:
            self.textBrowser_detailsAbonne.append(elt.__str__())


#################### CODE UTILISÉ: ###################
# Fichier de code : Exercice 1 - Interface graphique #
# Par : Hasna Hocini                                 #
######################################################

    # serealiser un abonné
    @pyqtSlot()
    def on_pushButton_serealiserAbonne_clicked(self):
        """
        Gestionnaire d'événement pour le bouton serealiserAbonne
        """
        # appel de la fonction cacher_labels_erreur
        cacher_labels_erreur(self)
        # instancier les attributs de la classe Abonne et l'objet Abonne
        abonneBiblio = Abonne()
        abonneBiblio.NumeroAbonne = self.lineEdit_numeroAbonne.text()
        abonneBiblio.PrenomAbonne = self.lineEdit_prenomAbonne.text().capitalize()
        abonneBiblio.NomAbonne = self.lineEdit_nomAbonne.text().capitalize()
        abonneBiblio.DateNaissAbonne = self.dateEdit_dateNaissAbonne.date()

        # si toutes les infos entrées sont valides
        if abonneBiblio.NumeroAbonne != "" and abonneBiblio.PrenomAbonne != "" and abonneBiblio.NomAbonne != "" and \
            abonneBiblio.DateNaissAbonne != "" :
            # séréaliser l'objet
            resultat = abonneBiblio.serialiserAbonne("." + "/" + "Serealiser" + "/" + abonneBiblio.NumeroAbonne + "_"
                                                     + abonneBiblio.PrenomAbonne + "_" + abonneBiblio.NomAbonne +
                                                     ".json")
            # si la séréalisation fonctionne
            if resultat == 0:
                # vider les line edits
                self.lineEdit_numeroAbonne.clear()
                self.lineEdit_prenomAbonne.clear()
                self.lineEdit_nomAbonne.clear()
                self.dateEdit_dateNaissAbonne.setDate(QDate(2000, 1, 1))
            # sinon afficher des messages d'erreur
            elif resultat == 1:
                # Afficher le message d'erreur d'écriture dans le fichier
                self.textBrowser_detailsAbonne.setText("Erreur d'écriture")
            else:
                # Afficher le message d'erreur d'ouverture du fichier
                self.textBrowser_detailsAbonne.setText("Erreur d'ouverture")

        # si le numéro de l'abonné est invalide, afficher un message d'erreur et vider le line edit du numéro
        if abonneBiblio.NumeroAbonne == "":
            self.lineEdit_numeroAbonne.clear()
            self.label_erreurNumeroAbonneInvalide.setVisible(True)

        # si le prenom de l'abonné est invalide, afficher un message d'erreur et vider le line edit du prenom
        if abonneBiblio.PrenomAbonne == "":
            self.lineEdit_prenomAbonne.clear()
            self.label_erreurPrenomInvalide.setVisible(True)

        # si le prenom de l'abonné est invalide, afficher un message d'erreur et vider le line edit du prenom
        if abonneBiblio.NomAbonne == "":
            self.lineEdit_nomAbonne.clear()
            self.label_erreurNomInvalide.setVisible(True)

        # si la date de naissance de l'abonné est invalide, afficher un message d'erreur
        if abonneBiblio.DateNaissAbonne == "":
            self.label_erreurDateNaissInvalide.setVisible(True)


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
        chaine = ""
        # pour chaque abonné dans la liste des abonnés
        for elt in liste_abonnes:
            # ajouter les abonnés à la chaine
            chaine += elt.__str__()
        try:
            with open("." + "/" + "listeAbonnes"+"/"+"ListeAbonnes.txt", "w") as fichier:
                try :
                    fichier.write(chaine)

                except :
                    self.textBrowser_detailsAbonne.setText("Erreur d'écriture")
        except :
            self.textBrowser_detailsAbonne.setText("Erreur d'ouverture")


    # quitter la fenêtre FenetreAbonne
    @pyqtSlot()
    def on_pushButton_quitterAbonne_clicked(self):
        """
        Gestionnaire d'événement pour le bouton quitterAbonne
        """
        self.close()
        print("Bouton quitterAbonne OK")

