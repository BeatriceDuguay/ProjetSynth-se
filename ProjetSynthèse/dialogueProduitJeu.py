# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogueProduitJeu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(809, 673)
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
        self.line_jeu1 = QtWidgets.QFrame(Dialog)
        self.line_jeu1.setGeometry(QtCore.QRect(250, 30, 3, 61))
        self.line_jeu1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_jeu1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_jeu1.setObjectName("line_jeu1")
        self.line_jeu2 = QtWidgets.QFrame(Dialog)
        self.line_jeu2.setGeometry(QtCore.QRect(250, 20, 311, 20))
        self.line_jeu2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_jeu2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_jeu2.setObjectName("line_jeu2")
        self.line_jeu4 = QtWidgets.QFrame(Dialog)
        self.line_jeu4.setGeometry(QtCore.QRect(250, 80, 311, 20))
        self.line_jeu4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_jeu4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_jeu4.setObjectName("line_jeu4")
        self.line_jeu3 = QtWidgets.QFrame(Dialog)
        self.line_jeu3.setGeometry(QtCore.QRect(560, 30, 3, 61))
        self.line_jeu3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_jeu3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_jeu3.setObjectName("line_jeu3")
        self.lineEdit_developpeurJeu = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_developpeurJeu.setGeometry(QtCore.QRect(110, 400, 251, 41))
        self.lineEdit_developpeurJeu.setObjectName("lineEdit_developpeurJeu")
        self.lineEdit_moteurJeu = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_moteurJeu.setGeometry(QtCore.QRect(450, 180, 251, 41))
        self.lineEdit_moteurJeu.setObjectName("lineEdit_moteurJeu")
        self.comboBox_consoleJeu = QtWidgets.QComboBox(Dialog)
        self.comboBox_consoleJeu.setGeometry(QtCore.QRect(450, 290, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.comboBox_consoleJeu.setFont(font)
        self.comboBox_consoleJeu.setObjectName("comboBox_consoleJeu")
        self.comboBox_consoleJeu.addItem("")
        self.comboBox_consoleJeu.addItem("")
        self.comboBox_consoleJeu.addItem("")
        self.comboBox_consoleJeu.addItem("")
        self.comboBox_consoleJeu.addItem("")
        self.comboBox_consoleJeu.addItem("")
        self.comboBox_consoleJeu.addItem("")
        self.comboBox_consoleJeu.addItem("")
        self.label_titreEmprunt = QtWidgets.QLabel(Dialog)
        self.label_titreEmprunt.setGeometry(QtCore.QRect(390, 20, 41, 81))
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
        self.label_titreEmprunt.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_titreEmprunt.setFont(font)
        self.label_titreEmprunt.setObjectName("label_titreEmprunt")
        self.label_erreurDeveloppeurJeuInvalide = QtWidgets.QLabel(Dialog)
        self.label_erreurDeveloppeurJeuInvalide.setGeometry(QtCore.QRect(110, 440, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurDeveloppeurJeuInvalide.setFont(font)
        self.label_erreurDeveloppeurJeuInvalide.setObjectName("label_erreurDeveloppeurJeuInvalide")
        self.label_erreurMoteurJeuInvalide = QtWidgets.QLabel(Dialog)
        self.label_erreurMoteurJeuInvalide.setGeometry(QtCore.QRect(450, 220, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurMoteurJeuInvalide.setFont(font)
        self.label_erreurMoteurJeuInvalide.setObjectName("label_erreurMoteurJeuInvalide")
        self.label_moteurJeu = QtWidgets.QLabel(Dialog)
        self.label_moteurJeu.setGeometry(QtCore.QRect(450, 140, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_moteurJeu.setFont(font)
        self.label_moteurJeu.setObjectName("label_moteurJeu")
        self.label_developpeurJeu = QtWidgets.QLabel(Dialog)
        self.label_developpeurJeu.setGeometry(QtCore.QRect(110, 360, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_developpeurJeu.setFont(font)
        self.label_developpeurJeu.setObjectName("label_developpeurJeu")
        self.label_consoleJeu = QtWidgets.QLabel(Dialog)
        self.label_consoleJeu.setGeometry(QtCore.QRect(450, 250, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_consoleJeu.setFont(font)
        self.label_consoleJeu.setObjectName("label_consoleJeu")
        self.pushButton_quitterJeu = QtWidgets.QPushButton(Dialog)
        self.pushButton_quitterJeu.setGeometry(QtCore.QRect(440, 520, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.pushButton_quitterJeu.setFont(font)
        self.pushButton_quitterJeu.setObjectName("pushButton_quitterJeu")
        self.pushButton_ajouterJeu = QtWidgets.QPushButton(Dialog)
        self.pushButton_ajouterJeu.setGeometry(QtCore.QRect(240, 520, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.pushButton_ajouterJeu.setFont(font)
        self.pushButton_ajouterJeu.setObjectName("pushButton_ajouterJeu")
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
        self.label_erreurNumeroSerieInvalide = QtWidgets.QLabel(Dialog)
        self.label_erreurNumeroSerieInvalide.setGeometry(QtCore.QRect(110, 340, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurNumeroSerieInvalide.setFont(font)
        self.label_erreurNumeroSerieInvalide.setObjectName("label_erreurNumeroSerieInvalide")
        self.label_erreurNumeroSerieInexistant = QtWidgets.QLabel(Dialog)
        self.label_erreurNumeroSerieInexistant.setGeometry(QtCore.QRect(110, 340, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurNumeroSerieInexistant.setFont(font)
        self.label_erreurNumeroSerieInexistant.setObjectName("label_erreurNumeroSerieInexistant")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox_consoleJeu.setItemText(0, _translate("Dialog", "PC MAC"))
        self.comboBox_consoleJeu.setItemText(1, _translate("Dialog", "PC WINDOWS"))
        self.comboBox_consoleJeu.setItemText(2, _translate("Dialog", "PS2"))
        self.comboBox_consoleJeu.setItemText(3, _translate("Dialog", "PS3"))
        self.comboBox_consoleJeu.setItemText(4, _translate("Dialog", "PS4"))
        self.comboBox_consoleJeu.setItemText(5, _translate("Dialog", "PS5"))
        self.comboBox_consoleJeu.setItemText(6, _translate("Dialog", "XBOX ONE"))
        self.comboBox_consoleJeu.setItemText(7, _translate("Dialog", "XBOX 360"))
        self.label_titreEmprunt.setText(_translate("Dialog", "JEU"))
        self.label_erreurDeveloppeurJeuInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le d??veloppeur du jeu est invalide</span></p></body></html>"))
        self.label_erreurMoteurJeuInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le moteur du jeu est invalide</span></p></body></html>"))
        self.label_moteurJeu.setText(_translate("Dialog", "Moteur du jeu"))
        self.label_developpeurJeu.setText(_translate("Dialog", "D??veloppeur du jeu"))
        self.label_consoleJeu.setText(_translate("Dialog", "Console"))
        self.pushButton_quitterJeu.setText(_translate("Dialog", "Quitter"))
        self.pushButton_ajouterJeu.setText(_translate("Dialog", "Ajouter"))
        self.label_numeroDetailEmprunt.setText(_translate("Dialog", "Num??ro du d??tail de l\'emprunt"))
        self.label_erreurNumeroDetailEmpruntInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le num??ro du d??tail de l\'emprunt est invalide</span></p></body></html>"))
        self.label_erreurNumeroDetailEmpruntInexistant.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le num??ro du d??tail de l\'emprunt est inexistant</span></p></body></html>"))
        self.label_numeroSerieProduit.setText(_translate("Dialog", "Num??ro de s??rie"))
        self.label_erreurNumeroSerieInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le num??ro de s??rie est invalide</span></p><p><br/></p></body></html>"))
        self.label_erreurNumeroSerieInexistant.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le num??ro de s??rie est inexistant</span></p><p><br/></p></body></html>"))
