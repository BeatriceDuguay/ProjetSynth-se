# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogueDetailsEmprunt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(808, 851)
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
        self.label_titreDetailsEmprunt = QtWidgets.QLabel(Dialog)
        self.label_titreDetailsEmprunt.setGeometry(QtCore.QRect(270, 20, 251, 81))
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
        self.label_titreDetailsEmprunt.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_titreDetailsEmprunt.setFont(font)
        self.label_titreDetailsEmprunt.setObjectName("label_titreDetailsEmprunt")
        self.line_detailsEmprunt3 = QtWidgets.QFrame(Dialog)
        self.line_detailsEmprunt3.setGeometry(QtCore.QRect(550, 30, 3, 61))
        self.line_detailsEmprunt3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_detailsEmprunt3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_detailsEmprunt3.setObjectName("line_detailsEmprunt3")
        self.line_detailsEmprunt2 = QtWidgets.QFrame(Dialog)
        self.line_detailsEmprunt2.setGeometry(QtCore.QRect(240, 20, 311, 20))
        self.line_detailsEmprunt2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_detailsEmprunt2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_detailsEmprunt2.setObjectName("line_detailsEmprunt2")
        self.line_detailsEmprunt4 = QtWidgets.QFrame(Dialog)
        self.line_detailsEmprunt4.setGeometry(QtCore.QRect(240, 80, 311, 20))
        self.line_detailsEmprunt4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_detailsEmprunt4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_detailsEmprunt4.setObjectName("line_detailsEmprunt4")
        self.line_detailsEmprunt1 = QtWidgets.QFrame(Dialog)
        self.line_detailsEmprunt1.setGeometry(QtCore.QRect(240, 30, 3, 61))
        self.line_detailsEmprunt1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_detailsEmprunt1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_detailsEmprunt1.setObjectName("line_detailsEmprunt1")
        self.lineEdit_numeroDetailEmprunt = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_numeroDetailEmprunt.setGeometry(QtCore.QRect(110, 290, 251, 41))
        self.lineEdit_numeroDetailEmprunt.setObjectName("lineEdit_numeroDetailEmprunt")
        self.label_numeroDetailEmprunt = QtWidgets.QLabel(Dialog)
        self.label_numeroDetailEmprunt.setGeometry(QtCore.QRect(110, 250, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_numeroDetailEmprunt.setFont(font)
        self.label_numeroDetailEmprunt.setObjectName("label_numeroDetailEmprunt")
        self.lineEdit_quantiteProduit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_quantiteProduit.setGeometry(QtCore.QRect(110, 400, 251, 41))
        self.lineEdit_quantiteProduit.setObjectName("lineEdit_quantiteProduit")
        self.lineEdit_titreProduit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_titreProduit.setGeometry(QtCore.QRect(450, 180, 251, 41))
        self.lineEdit_titreProduit.setObjectName("lineEdit_titreProduit")
        self.comboBox_typeProduit = QtWidgets.QComboBox(Dialog)
        self.comboBox_typeProduit.setGeometry(QtCore.QRect(110, 510, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.comboBox_typeProduit.setFont(font)
        self.comboBox_typeProduit.setObjectName("comboBox_typeProduit")
        self.comboBox_typeProduit.addItem("")
        self.comboBox_typeProduit.addItem("")
        self.comboBox_typeProduit.addItem("")
        self.lineEdit_numeroSerieProduit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_numeroSerieProduit.setGeometry(QtCore.QRect(110, 620, 251, 41))
        self.lineEdit_numeroSerieProduit.setObjectName("lineEdit_numeroSerieProduit")
        self.lineEdit_genreProduit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_genreProduit.setGeometry(QtCore.QRect(450, 510, 251, 41))
        self.lineEdit_genreProduit.setObjectName("lineEdit_genreProduit")
        self.lineEdit_langueOrigineProduit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_langueOrigineProduit.setGeometry(QtCore.QRect(450, 290, 251, 41))
        self.lineEdit_langueOrigineProduit.setObjectName("lineEdit_langueOrigineProduit")
        self.lineEdit_anneeSortieProduit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_anneeSortieProduit.setGeometry(QtCore.QRect(450, 400, 251, 41))
        self.lineEdit_anneeSortieProduit.setObjectName("lineEdit_anneeSortieProduit")
        self.label_quantiteProduit = QtWidgets.QLabel(Dialog)
        self.label_quantiteProduit.setGeometry(QtCore.QRect(110, 360, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_quantiteProduit.setFont(font)
        self.label_quantiteProduit.setObjectName("label_quantiteProduit")
        self.label_typeProduit = QtWidgets.QLabel(Dialog)
        self.label_typeProduit.setGeometry(QtCore.QRect(110, 470, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_typeProduit.setFont(font)
        self.label_typeProduit.setObjectName("label_typeProduit")
        self.label_numeroSerieProduit = QtWidgets.QLabel(Dialog)
        self.label_numeroSerieProduit.setGeometry(QtCore.QRect(110, 580, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_numeroSerieProduit.setFont(font)
        self.label_numeroSerieProduit.setObjectName("label_numeroSerieProduit")
        self.label_titreProduit = QtWidgets.QLabel(Dialog)
        self.label_titreProduit.setGeometry(QtCore.QRect(450, 140, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_titreProduit.setFont(font)
        self.label_titreProduit.setObjectName("label_titreProduit")
        self.label_langueOrigineProduit = QtWidgets.QLabel(Dialog)
        self.label_langueOrigineProduit.setGeometry(QtCore.QRect(450, 250, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_langueOrigineProduit.setFont(font)
        self.label_langueOrigineProduit.setObjectName("label_langueOrigineProduit")
        self.label_anneeSortieProduit = QtWidgets.QLabel(Dialog)
        self.label_anneeSortieProduit.setGeometry(QtCore.QRect(450, 360, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_anneeSortieProduit.setFont(font)
        self.label_anneeSortieProduit.setObjectName("label_anneeSortieProduit")
        self.label_genreProduit = QtWidgets.QLabel(Dialog)
        self.label_genreProduit.setGeometry(QtCore.QRect(450, 470, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_genreProduit.setFont(font)
        self.label_genreProduit.setObjectName("label_genreProduit")
        self.pushButton_produit = QtWidgets.QPushButton(Dialog)
        self.pushButton_produit.setGeometry(QtCore.QRect(240, 740, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.pushButton_produit.setFont(font)
        self.pushButton_produit.setObjectName("pushButton_produit")
        self.label_erreurNumeroDetailEmpruntInvalide = QtWidgets.QLabel(Dialog)
        self.label_erreurNumeroDetailEmpruntInvalide.setGeometry(QtCore.QRect(110, 330, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurNumeroDetailEmpruntInvalide.setFont(font)
        self.label_erreurNumeroDetailEmpruntInvalide.setObjectName("label_erreurNumeroDetailEmpruntInvalide")
        self.label_erreurNumeroDetailEmpruntExiste = QtWidgets.QLabel(Dialog)
        self.label_erreurNumeroDetailEmpruntExiste.setGeometry(QtCore.QRect(110, 330, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurNumeroDetailEmpruntExiste.setFont(font)
        self.label_erreurNumeroDetailEmpruntExiste.setObjectName("label_erreurNumeroDetailEmpruntExiste")
        self.label_erreurQuantiteProduitInvalide = QtWidgets.QLabel(Dialog)
        self.label_erreurQuantiteProduitInvalide.setGeometry(QtCore.QRect(110, 440, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurQuantiteProduitInvalide.setFont(font)
        self.label_erreurQuantiteProduitInvalide.setObjectName("label_erreurQuantiteProduitInvalide")
        self.label_erreurNumeroSerieInvalide = QtWidgets.QLabel(Dialog)
        self.label_erreurNumeroSerieInvalide.setGeometry(QtCore.QRect(110, 670, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurNumeroSerieInvalide.setFont(font)
        self.label_erreurNumeroSerieInvalide.setObjectName("label_erreurNumeroSerieInvalide")
        self.label_erreurNumeroSerieExiste = QtWidgets.QLabel(Dialog)
        self.label_erreurNumeroSerieExiste.setGeometry(QtCore.QRect(110, 670, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurNumeroSerieExiste.setFont(font)
        self.label_erreurNumeroSerieExiste.setObjectName("label_erreurNumeroSerieExiste")
        self.label_erreurTitreProduitInvalide = QtWidgets.QLabel(Dialog)
        self.label_erreurTitreProduitInvalide.setGeometry(QtCore.QRect(450, 220, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurTitreProduitInvalide.setFont(font)
        self.label_erreurTitreProduitInvalide.setObjectName("label_erreurTitreProduitInvalide")
        self.label_erreurLangueOrigineInvalide = QtWidgets.QLabel(Dialog)
        self.label_erreurLangueOrigineInvalide.setGeometry(QtCore.QRect(450, 330, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurLangueOrigineInvalide.setFont(font)
        self.label_erreurLangueOrigineInvalide.setObjectName("label_erreurLangueOrigineInvalide")
        self.label_erreurAnneeSortieInvalide = QtWidgets.QLabel(Dialog)
        self.label_erreurAnneeSortieInvalide.setGeometry(QtCore.QRect(450, 440, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurAnneeSortieInvalide.setFont(font)
        self.label_erreurAnneeSortieInvalide.setObjectName("label_erreurAnneeSortieInvalide")
        self.label_erreurGenreProduitInvalide = QtWidgets.QLabel(Dialog)
        self.label_erreurGenreProduitInvalide.setGeometry(QtCore.QRect(450, 550, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurGenreProduitInvalide.setFont(font)
        self.label_erreurGenreProduitInvalide.setObjectName("label_erreurGenreProduitInvalide")
        self.pushButton_quitterDetailsEmprunt = QtWidgets.QPushButton(Dialog)
        self.pushButton_quitterDetailsEmprunt.setGeometry(QtCore.QRect(440, 740, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.pushButton_quitterDetailsEmprunt.setFont(font)
        self.pushButton_quitterDetailsEmprunt.setObjectName("pushButton_quitterDetailsEmprunt")
        self.lineEdit_numeroEmprunt = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_numeroEmprunt.setGeometry(QtCore.QRect(110, 180, 251, 41))
        self.lineEdit_numeroEmprunt.setObjectName("lineEdit_numeroEmprunt")
        self.label_numeroEmprunt = QtWidgets.QLabel(Dialog)
        self.label_numeroEmprunt.setGeometry(QtCore.QRect(110, 140, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.label_numeroEmprunt.setFont(font)
        self.label_numeroEmprunt.setObjectName("label_numeroEmprunt")
        self.label_erreurNumeroEmpruntInexistant = QtWidgets.QLabel(Dialog)
        self.label_erreurNumeroEmpruntInexistant.setGeometry(QtCore.QRect(110, 220, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurNumeroEmpruntInexistant.setFont(font)
        self.label_erreurNumeroEmpruntInexistant.setObjectName("label_erreurNumeroEmpruntInexistant")
        self.label_erreurNumeroEmpruntInvalide = QtWidgets.QLabel(Dialog)
        self.label_erreurNumeroEmpruntInvalide.setGeometry(QtCore.QRect(110, 220, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_erreurNumeroEmpruntInvalide.setFont(font)
        self.label_erreurNumeroEmpruntInvalide.setObjectName("label_erreurNumeroEmpruntInvalide")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_titreDetailsEmprunt.setText(_translate("Dialog", "DÉTAILS DE L\'EMPRUNT"))
        self.label_numeroDetailEmprunt.setText(_translate("Dialog", "Numéro du détail de l\'emprunt"))
        self.comboBox_typeProduit.setItemText(0, _translate("Dialog", "Film"))
        self.comboBox_typeProduit.setItemText(1, _translate("Dialog", "Jeu"))
        self.comboBox_typeProduit.setItemText(2, _translate("Dialog", "Livre"))
        self.label_quantiteProduit.setText(_translate("Dialog", "Quantité du produit"))
        self.label_typeProduit.setText(_translate("Dialog", "Type du produit"))
        self.label_numeroSerieProduit.setText(_translate("Dialog", "Numéro de série"))
        self.label_titreProduit.setText(_translate("Dialog", "Titre du produit"))
        self.label_langueOrigineProduit.setText(_translate("Dialog", "Langue d\'origine"))
        self.label_anneeSortieProduit.setText(_translate("Dialog", "Année de sortie "))
        self.label_genreProduit.setText(_translate("Dialog", "Genre"))
        self.pushButton_produit.setText(_translate("Dialog", "Détails produit"))
        self.label_erreurNumeroDetailEmpruntInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le numéro du détail de l\'emprunt est invalide</span></p></body></html>"))
        self.label_erreurNumeroDetailEmpruntExiste.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le numéro du détail de l\'emprunt existe déjà</span></p></body></html>"))
        self.label_erreurQuantiteProduitInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">La quantité du produit est invalide</span></p></body></html>"))
        self.label_erreurNumeroSerieInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le numéro de série est invalide</span></p><p><br/></p></body></html>"))
        self.label_erreurNumeroSerieExiste.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le numéro de série existe déjà</span></p><p><br/></p></body></html>"))
        self.label_erreurTitreProduitInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le titre du produit est invalide</span></p></body></html>"))
        self.label_erreurLangueOrigineInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">La langue d\'origine est invalide</span></p></body></html>"))
        self.label_erreurAnneeSortieInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">L\'année de sortie est invalide</span></p></body></html>"))
        self.label_erreurGenreProduitInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le genre du produit est invalide</span></p></body></html>"))
        self.pushButton_quitterDetailsEmprunt.setText(_translate("Dialog", "Quitter"))
        self.label_numeroEmprunt.setText(_translate("Dialog", "Numéro de l\'emprunt"))
        self.label_erreurNumeroEmpruntInexistant.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le numéro de l\'emprunt est inexistant</span></p></body></html>"))
        self.label_erreurNumeroEmpruntInvalide.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">Le numéro de l\'emprunt est invalide</span></p></body></html>"))
