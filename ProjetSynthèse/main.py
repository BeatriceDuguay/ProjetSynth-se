#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################

# les listes


# début 11h à 3h = 4h
# début 1h15 à 3h = 1h45
# 11h à 15h15 = 4h15
# 4h20 à 7h = 2h40
# 8h à 11h = 3h
# 5h à 7h = 2h
# 8h à 12h = 5h
# 11h à 3h = 4h
# 11h40 à = 6h
# importer le module sys nécessaire à l'execution.
import sys

# pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# importer l'interface graphique
import interfacegraphique

# importer les classes de dialogue
from FenetreAbonne import *
from FenetreEmprunt import *

####################################################################
###### DÉFINITIONS DE LA CLASSE fenetrePrincipaleBibliotheque ######
####################################################################

# Créer une classe qui hérite de Qt et de notre ui.
# Nom de ma classe (fenetrePrincipaleBibliotheque)          # Nom de mon fichier ui
class fenetrePrincipaleBibliotheque(QtWidgets.QMainWindow, interfacegraphique.Ui_MainWindow):
    """
    Nome de la classe : fenetrePrincipaleBibliothèque
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - interfacegraphique.Ui_MainWindow : Ma classe générée avec QtDesigner
    """
    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et ProjetIntra_MainWindow.Ui_MainWindow
        """
        # appel du constructeur parent
        super(fenetrePrincipaleBibliotheque, self).__init__(parent)
        # préparer l'interface graphique
        self.setupUi(self)
        # changer le nom de la fenêtre principale
        self.setWindowTitle("Gestion des emprunts de la bibliothèque")

    # ouvrir la fenêtre FenetreAbonne
    @pyqtSlot()
    def on_pushButton_gestionAbonnes_clicked(self):
        """
        Gestionnaire d'événement pour le bouton gestionAbonnes
        """
        # instancier la boîte de dialogue FenetreAbonne
        dialog = FenetreAbonne()
        # afficher la boîte
        dialog.show()
        reply=dialog.exec_()
        print("Bouton gestionAbonnes OK")

    # ouvrir la fenêtre FenetreEmprunt
    @pyqtSlot()
    def on_pushButton_gestionEmprunts_clicked(self):
        """
        Gestionnaire d'événement pour le bouton gestionEmprunts
        """
        # instancier la boîte de dialogue FenetreEmprunt
        dialog = FenetreEmprunt()
        # afficher la boîte
        dialog.show()
        reply=dialog.exec_()
        print("Bouton gestionEmprunts OK")

    # fermer la fenêtre fenetrePrincipaleBibliotheque
    @pyqtSlot()
    def on_pushButton_quitterMain_clicked(self):
        """
        Gestionnaire d'événement pour le bouton quitterMain
        """
        self.close()
        print("Bouton quitterMain OK")


#############################
###  PROGRAMME PRINCIPAL  ###
#############################

def Main():
    """
    Méthode Main : permet d'utiliser l'application et affiche la fenêtre principale
    reply = Dialog.exec_()
    """
    # instancier la fenêtre principale
    app = QtWidgets.QApplication(sys.argv)
    form = fenetrePrincipaleBibliotheque()
    # afficher la fenêtre principale
    form.show()
    # lancer l'application QtDesigner
    app.exec()

if __name__ == "__main__":
    Main()


