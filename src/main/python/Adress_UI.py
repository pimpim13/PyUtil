# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/alainzypinoglou/PycharmProjects/PyUtil/src/main/python/package/Adress_UI.ui',
# licensing of '/Users/alainzypinoglou/PycharmProjects/PyUtil/src/main/python/package/Adress_UI.ui' applies.
#
# Created: Sat Feb  1 09:15:18 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(609, 388)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_import_ref = QtWidgets.QPushButton(Form)
        self.btn_import_ref.setObjectName("btn_import_ref")
        self.gridLayout.addWidget(self.btn_import_ref, 5, 1, 1, 1)
        self.btn_generate_list = QtWidgets.QPushButton(Form)
        self.btn_generate_list.setObjectName("btn_generate_list")
        self.gridLayout.addWidget(self.btn_generate_list, 12, 1, 1, 4)
        self.btn_convert_ref = QtWidgets.QPushButton(Form)
        self.btn_convert_ref.setObjectName("btn_convert_ref")
        self.gridLayout.addWidget(self.btn_convert_ref, 3, 1, 1, 1)
        self.lw_liste_ref = QtWidgets.QListWidget(Form)
        self.lw_liste_ref.setObjectName("lw_liste_ref")
        self.gridLayout.addWidget(self.lw_liste_ref, 7, 1, 4, 1)
        self.btn_convert_exclusion = QtWidgets.QPushButton(Form)
        self.btn_convert_exclusion.setObjectName("btn_convert_exclusion")
        self.gridLayout.addWidget(self.btn_convert_exclusion, 3, 3, 1, 2)
        self.lw_liste_exclusion = QtWidgets.QListWidget(Form)
        self.lw_liste_exclusion.setObjectName("lw_liste_exclusion")
        self.gridLayout.addWidget(self.lw_liste_exclusion, 7, 3, 4, 2)
        self.btn_import_exclusion = QtWidgets.QPushButton(Form)
        self.btn_import_exclusion.setObjectName("btn_import_exclusion")
        self.gridLayout.addWidget(self.btn_import_exclusion, 5, 3, 1, 2)
        self.btn_exclude = QtWidgets.QPushButton(Form)
        self.btn_exclude.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_exclude.setFlat(False)
        self.btn_exclude.setObjectName("btn_exclude")
        self.gridLayout.addWidget(self.btn_exclude, 8, 2, 1, 1)
        self.btn_include = QtWidgets.QPushButton(Form)
        self.btn_include.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_include.setObjectName("btn_include")
        self.gridLayout.addWidget(self.btn_include, 9, 2, 1, 1)
        self.btn_open_exclusion = QtWidgets.QPushButton(Form)
        self.btn_open_exclusion.setObjectName("btn_open_exclusion")
        self.gridLayout.addWidget(self.btn_open_exclusion, 1, 3, 1, 2)
        self.btn_open_ref = QtWidgets.QPushButton(Form)
        self.btn_open_ref.setObjectName("btn_open_ref")
        self.gridLayout.addWidget(self.btn_open_ref, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Gestion d\'exclusion", None, -1))
        self.btn_import_ref.setText(QtWidgets.QApplication.translate("Form", "Importer json", None, -1))
        self.btn_generate_list.setText(QtWidgets.QApplication.translate("Form", "Generer Liste", None, -1))
        self.btn_convert_ref.setText(QtWidgets.QApplication.translate("Form", "Sauvegarder", None, -1))
        self.btn_convert_exclusion.setText(QtWidgets.QApplication.translate("Form", "convertir", None, -1))
        self.btn_import_exclusion.setText(QtWidgets.QApplication.translate("Form", "Importer Exclusion", None, -1))
        self.btn_exclude.setText(QtWidgets.QApplication.translate("Form", "->", None, -1))
        self.btn_include.setText(QtWidgets.QApplication.translate("Form", "<-", None, -1))
        self.btn_open_exclusion.setText(QtWidgets.QApplication.translate("Form", "Importer Nouvelle Exclusion", None, -1))
        self.btn_open_ref.setText(QtWidgets.QApplication.translate("Form", "Importer Nouvelle Ref ", None, -1))

