# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogueProduitLivre.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(808, 671)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 227, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 241, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 113, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 151, 151))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 227, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 241, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 227, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 241, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 113, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 151, 151))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 227, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 241, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 113, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 227, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 241, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 113, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 151, 151))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 113, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 113, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 227, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 227, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 227, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        Dialog.setPalette(palette)
        self.line_livre1 = QtWidgets.QFrame(Dialog)
        self.line_livre1.setGeometry(QtCore.QRect(250, 30, 3, 61))
        self.line_livre1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_livre1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_livre1.setObjectName("line_livre1")
        self.line_livre3 = QtWidgets.QFrame(Dialog)
        self.line_livre3.setGeometry(QtCore.QRect(560, 30, 3, 61))
        self.line_livre3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_livre3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_livre3.setObjectName("line_livre3")
        self.line_livre2 = QtWidgets.QFrame(Dialog)
        self.line_livre2.setGeometry(QtCore.QRect(250, 20, 311, 20))
        self.line_livre2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_livre2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_livre2.setObjectName("line_livre2")
        self.line_livre4 = QtWidgets.QFrame(Dialog)
        self.line_livre4.setGeometry(QtCore.QRect(250, 80, 311, 20))
        self.line_livre4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_livre4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_livre4.setObjectName("line_livre4")
        self.lineEdit_prenomAuteur = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_prenomAuteur.setGeometry(QtCore.QRect(450, 290, 251, 41))
        self.lineEdit_prenomAuteur.setObjectName("lineEdit_prenomAuteur")
        self.lineEdit_nombrePages = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nombrePages.setGeometry(QtCore.QRect(450, 180, 251, 41))
        self.lineEdit_nombrePages.setObjectName("lineEdit_nombrePages")
        self.lineEdit_maisonEdition = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_maisonEdition.setGeometry(QtCore.QRect(110, 400, 251, 41))
        self.lineEdit_maisonEdition.setObjectName("lineEdit_maisonEdition")
        self.lineEdit_nomAuteur = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nomAuteur.setGeometry(QtCore.QRect(450, 400, 251, 41))
        self.lineEdit_nomAuteur.setObjectName("lineEdit_nomAuteur")
        self.label_titreLivre = QtWidgets.QLabel(Dialog)
        self.label_titreLivre.setGeometry(QtCore.QRect(380, 20, 61, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 121, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_titreLivre.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_titreLivre.setFont(font)
        self.label_titreLivre.setObjectName("label_titreLivre")
        self.label_erreurMaisonEditionInvalide = QtWidgets.QLabel(Dialog)
        self.label_erreurMaisonEditionInvalide.setGeometry(QtCore.QRect(110, 440, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurMaisonEditionInvalide.setFont(font)
        self.label_erreurMaisonEditionInvalide.setObjectName("label_erreurMaisonEditionInvalide")
        self.label_erreurNomAuteurInvalide = QtWidgets.QLabel(Dialog)
        self.label_erreurNomAuteurInvalide.setGeometry(QtCore.QRect(450, 440, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurNomAuteurInvalide.setFont(font)
        self.label_erreurNomAuteurInvalide.setObjectName("label_erreurNomAuteurInvalide")
        self.label_erreurNombrePagesInvalide = QtWidgets.QLabel(Dialog)
        self.label_erreurNombrePagesInvalide.setGeometry(QtCore.QRect(450, 220, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurNombrePagesInvalide.setFont(font)
        self.label_erreurNombrePagesInvalide.setObjectName("label_erreurNombrePagesInvalide")
        self.label_erreurPrenomAuteurInvalide = QtWidgets.QLabel(Dialog)
        self.label_erreurPrenomAuteurInvalide.setGeometry(QtCore.QRect(450, 330, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurPrenomAuteurInvalide.setFont(font)
        self.label_erreurPrenomAuteurInvalide.setObjectName("label_erreurPrenomAuteurInvalide")
        self.label_maisonEdition = QtWidgets.QLabel(Dialog)
        self.label_maisonEdition.setGeometry(QtCore.QRect(110, 360, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_maisonEdition.setFont(font)
        self.label_maisonEdition.setObjectName("label_maisonEdition")
        self.label_nomAuteur = QtWidgets.QLabel(Dialog)
        self.label_nomAuteur.setGeometry(QtCore.QRect(450, 360, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_nomAuteur.setFont(font)
        self.label_nomAuteur.setObjectName("label_nomAuteur")
        self.label_nombrePages = QtWidgets.QLabel(Dialog)
        self.label_nombrePages.setGeometry(QtCore.QRect(450, 140, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_nombrePages.setFont(font)
        self.label_nombrePages.setObjectName("label_nombrePages")
        self.label_prenomAuteur = QtWidgets.QLabel(Dialog)
        self.label_prenomAuteur.setGeometry(QtCore.QRect(450, 250, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_prenomAuteur.setFont(font)
        self.label_prenomAuteur.setObjectName("label_prenomAuteur")
        self.pushButton_quitterLivre = QtWidgets.QPushButton(Dialog)
        self.pushButton_quitterLivre.setGeometry(QtCore.QRect(250, 520, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.pushButton_quitterLivre.setFont(font)
        self.pushButton_quitterLivre.setObjectName("pushButton_quitterLivre")
        self.pushButton_ajouterLivre = QtWidgets.QPushButton(Dialog)
        self.pushButton_ajouterLivre.setGeometry(QtCore.QRect(80, 520, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.pushButton_ajouterLivre.setFont(font)
        self.pushButton_ajouterLivre.setObjectName("pushButton_ajouterLivre")
        self.pushButton_sauvegarderLivre = QtWidgets.QPushButton(Dialog)
        self.pushButton_sauvegarderLivre.setGeometry(QtCore.QRect(600, 520, 131, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 113, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.pushButton_sauvegarderLivre.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.pushButton_sauvegarderLivre.setFont(font)
        self.pushButton_sauvegarderLivre.setObjectName("pushButton_sauvegarderLivre")
        self.pushButton_serealiserLivre = QtWidgets.QPushButton(Dialog)
        self.pushButton_serealiserLivre.setGeometry(QtCore.QRect(430, 520, 131, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 113, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.pushButton_serealiserLivre.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.pushButton_serealiserLivre.setFont(font)
        self.pushButton_serealiserLivre.setObjectName("pushButton_serealiserLivre")
        self.lineEdit_numeroDetailEmprunt = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_numeroDetailEmprunt.setGeometry(QtCore.QRect(110, 180, 251, 41))
        self.lineEdit_numeroDetailEmprunt.setObjectName("lineEdit_numeroDetailEmprunt")
        self.label_numeroDetailEmprunt = QtWidgets.QLabel(Dialog)
        self.label_numeroDetailEmprunt.setGeometry(QtCore.QRect(110, 140, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_numeroDetailEmprunt.setFont(font)
        self.label_numeroDetailEmprunt.setObjectName("label_numeroDetailEmprunt")
        self.label_erreurNumeroDetailEmpruntInvalide = QtWidgets.QLabel(Dialog)
        self.label_erreurNumeroDetailEmpruntInvalide.setGeometry(QtCore.QRect(110, 220, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurNumeroDetailEmpruntInvalide.setFont(font)
        self.label_erreurNumeroDetailEmpruntInvalide.setObjectName("label_erreurNumeroDetailEmpruntInvalide")
        self.label_erreurNumeroDetailEmpruntInexistant = QtWidgets.QLabel(Dialog)
        self.label_erreurNumeroDetailEmpruntInexistant.setGeometry(QtCore.QRect(110, 220, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurNumeroDetailEmpruntInexistant.setFont(font)
        self.label_erreurNumeroDetailEmpruntInexistant.setObjectName("label_erreurNumeroDetailEmpruntInexistant")
        self.label_erreurNumeroSerieInexistant = QtWidgets.QLabel(Dialog)
        self.label_erreurNumeroSerieInexistant.setGeometry(QtCore.QRect(110, 340, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurNumeroSerieInexistant.setFont(font)
        self.label_erreurNumeroSerieInexistant.setObjectName("label_erreurNumeroSerieInexistant")
        self.label_erreurNumeroSerieInvalide = QtWidgets.QLabel(Dialog)
        self.label_erreurNumeroSerieInvalide.setGeometry(QtCore.QRect(110, 340, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurNumeroSerieInvalide.setFont(font)
        self.label_erreurNumeroSerieInvalide.setObjectName("label_erreurNumeroSerieInvalide")
        self.lineEdit_numeroSerieProduit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_numeroSerieProduit.setGeometry(QtCore.QRect(110, 290, 251, 41))
        self.lineEdit_numeroSerieProduit.setObjectName("lineEdit_numeroSerieProduit")
        self.label_numeroSerieProduit = QtWidgets.QLabel(Dialog)
        self.label_numeroSerieProduit.setGeometry(QtCore.QRect(110, 250, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_numeroSerieProduit.setFont(font)
        self.label_numeroSerieProduit.setObjectName("label_numeroSerieProduit")
        self.label_erreurFichierLivre = QtWidgets.QLabel(Dialog)
        self.label_erreurFichierLivre.setGeometry(QtCore.QRect(390, 560, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurFichierLivre.setFont(font)
        self.label_erreurFichierLivre.setObjectName("label_erreurFichierLivre")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_titreLivre.setText(_translate("Dialog", "LIVRE"))
        self.label_erreurMaisonEditionInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">La maison d\'édition est invalide</span></p></body></html>"))
        self.label_erreurNomAuteurInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le nom de l\'auteur(e) est invalide</span></p></body></html>"))
        self.label_erreurNombrePagesInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le nombre de pages est invalide</span></p></body></html>"))
        self.label_erreurPrenomAuteurInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le prénom de l\'auteur(e) est invalide</span></p></body></html>"))
        self.label_maisonEdition.setText(_translate("Dialog", "Maison d\'édition"))
        self.label_nomAuteur.setText(_translate("Dialog", "Nom de l\'auteur(e)"))
        self.label_nombrePages.setText(_translate("Dialog", "Nombre de pages"))
        self.label_prenomAuteur.setText(_translate("Dialog", "Prénom de l\'auteur(e)"))
        self.pushButton_quitterLivre.setText(_translate("Dialog", "Quitter"))
        self.pushButton_ajouterLivre.setText(_translate("Dialog", "Ajouter"))
        self.pushButton_sauvegarderLivre.setText(_translate("Dialog", "Sauvegarder"))
        self.pushButton_serealiserLivre.setText(_translate("Dialog", "Séréaliser"))
        self.label_numeroDetailEmprunt.setText(_translate("Dialog", "Numéro du détail de l\'emprunt"))
        self.label_erreurNumeroDetailEmpruntInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le numéro du détail de l\'emprunt est invalide</span></p></body></html>"))
        self.label_erreurNumeroDetailEmpruntInexistant.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le numéro du détail de l\'emprunt est inexistant</span></p></body></html>"))
        self.label_erreurNumeroSerieInexistant.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le numéro de série est inexistant</span></p><p><br/></p></body></html>"))
        self.label_erreurNumeroSerieInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le numéro de série est invalide</span></p><p><br/></p></body></html>"))
        self.label_numeroSerieProduit.setText(_translate("Dialog", "Numéro de série"))
        self.label_erreurFichierLivre.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\"><br/></span></p></body></html>"))
