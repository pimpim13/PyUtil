# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/alainzypinoglou/PycharmProjects/PyUtil/src/main/python/package/Adress3_UI.ui',
# licensing of '/Users/alainzypinoglou/PycharmProjects/PyUtil/src/main/python/package/Adress3_UI.ui' applies.
#
# Created: Tue Mar 24 11:51:21 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(645, 534)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(6, 8, 631, 511))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_open_ref = QtWidgets.QPushButton(self.widget)
        self.btn_open_ref.setObjectName("btn_open_ref")
        self.gridLayout.addWidget(self.btn_open_ref, 0, 0, 1, 1)
        self.btn_open_exclusion = QtWidgets.QPushButton(self.widget)
        self.btn_open_exclusion.setObjectName("btn_open_exclusion")
        self.gridLayout.addWidget(self.btn_open_exclusion, 0, 2, 1, 1)
        self.btn_convert_ref = QtWidgets.QPushButton(self.widget)
        self.btn_convert_ref.setObjectName("btn_convert_ref")
        self.gridLayout.addWidget(self.btn_convert_ref, 1, 0, 1, 1)
        self.btn_convert_exclusion = QtWidgets.QPushButton(self.widget)
        self.btn_convert_exclusion.setObjectName("btn_convert_exclusion")
        self.gridLayout.addWidget(self.btn_convert_exclusion, 1, 2, 1, 1)
        self.cb_import_json = QtWidgets.QComboBox(self.widget)
        self.cb_import_json.setEditable(False)
        self.cb_import_json.setObjectName("cb_import_json")
        self.gridLayout.addWidget(self.cb_import_json, 2, 0, 1, 1)
        self.btn_import_exclusion = QtWidgets.QPushButton(self.widget)
        self.btn_import_exclusion.setObjectName("btn_import_exclusion")
        self.gridLayout.addWidget(self.btn_import_exclusion, 2, 2, 1, 1)
        self.btn_text_ref = QtWidgets.QPushButton(self.widget)
        self.btn_text_ref.setObjectName("btn_text_ref")
        self.gridLayout.addWidget(self.btn_text_ref, 3, 0, 1, 1)
        self.btn_text_exclusion = QtWidgets.QPushButton(self.widget)
        self.btn_text_exclusion.setObjectName("btn_text_exclusion")
        self.gridLayout.addWidget(self.btn_text_exclusion, 3, 2, 1, 1)
        self.pt_texte_brut = QtWidgets.QTextEdit(self.widget)
        self.pt_texte_brut.setObjectName("pt_texte_brut")
        self.gridLayout.addWidget(self.pt_texte_brut, 4, 0, 1, 3)
        self.lbl_dropinfo = QtWidgets.QLabel(self.widget)
        self.lbl_dropinfo.setEnabled(True)
        self.lbl_dropinfo.setObjectName("lbl_dropinfo")
        self.gridLayout.addWidget(self.lbl_dropinfo, 5, 0, 1, 1)
        self.lw_liste_ref = QtWidgets.QListWidget(self.widget)
        self.lw_liste_ref.setObjectName("lw_liste_ref")
        self.gridLayout.addWidget(self.lw_liste_ref, 6, 0, 2, 1)
        self.btn_include = QtWidgets.QPushButton(self.widget)
        self.btn_include.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_include.setObjectName("btn_include")
        self.gridLayout.addWidget(self.btn_include, 6, 1, 1, 1)
        self.lw_liste_exclusion = QtWidgets.QListWidget(self.widget)
        self.lw_liste_exclusion.setObjectName("lw_liste_exclusion")
        self.gridLayout.addWidget(self.lw_liste_exclusion, 6, 2, 2, 1)
        self.btn_exclude = QtWidgets.QPushButton(self.widget)
        self.btn_exclude.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_exclude.setFlat(False)
        self.btn_exclude.setObjectName("btn_exclude")
        self.gridLayout.addWidget(self.btn_exclude, 7, 1, 1, 1)
        self.btn_generate_list = QtWidgets.QPushButton(self.widget)
        self.btn_generate_list.setObjectName("btn_generate_list")
        self.gridLayout.addWidget(self.btn_generate_list, 8, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Gestion d\'exclusion", None, -1))
        self.btn_open_ref.setText(QtWidgets.QApplication.translate("Form", "Importer Nouvelle Ref ", None, -1))
        self.btn_open_exclusion.setText(QtWidgets.QApplication.translate("Form", "Importer Nouvelle Exclusion", None, -1))
        self.btn_convert_ref.setText(QtWidgets.QApplication.translate("Form", "Sauvegarder", None, -1))
        self.btn_convert_exclusion.setText(QtWidgets.QApplication.translate("Form", "Sauvegarder", None, -1))
        self.btn_import_exclusion.setText(QtWidgets.QApplication.translate("Form", "Importer Exclusion", None, -1))
        self.btn_text_ref.setText(QtWidgets.QApplication.translate("Form", "Convertir Texte", None, -1))
        self.btn_text_exclusion.setText(QtWidgets.QApplication.translate("Form", "Convertir Texte", None, -1))
        self.pt_texte_brut.setPlaceholderText(QtWidgets.QApplication.translate("Form", "glissez deposez ou collez le texte à convertir ici", None, -1))
        self.lbl_dropinfo.setText(QtWidgets.QApplication.translate("Form", "Déposez le texte dans l\'interface", None, -1))
        self.btn_include.setText(QtWidgets.QApplication.translate("Form", "<-", None, -1))
        self.btn_exclude.setText(QtWidgets.QApplication.translate("Form", "->", None, -1))
        self.btn_generate_list.setText(QtWidgets.QApplication.translate("Form", "Generer Liste", None, -1))

