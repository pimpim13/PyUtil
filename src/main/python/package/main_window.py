from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QToolButton

import package.API.Adress as Api
import os
import re
import logging
# from datetime import datetime

logging.basicConfig(level=logging.DEBUG)


class Window(QtWidgets.QMainWindow):

    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx
        self.setup_ui()

    def setup_ui(self):

        css_file = "../resources/base/style.css"
        if not os.path.exists(css_file):
            logging.error(f"Le fichier {css_file} est introuvable")
        else:
            # css_file = self.ctx.get_resource("style.css")
            with open(css_file, 'r') as f:
                self.setStyleSheet(f.read())

        lst_json = Api.get_lst_of_json(Api.ADRESS_DIR)
        self.w1 = MainWindow()
        self.setCentralWidget(self.w1)

        self.toolbar_A = self.addToolBar("Liste A")

        self.statusBar()

        self._openbutton = QToolButton()
        self._openbutton.setCheckable(False)
        self._openbutton.setChecked(False)
        self._openbutton.setAutoRaise(True)
        self._openbutton.setIcon(QtGui.QIcon("../icons/arrowA.png"))
        self._openbutton.setText("Open A")
        self._openbutton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self._openbutton.clicked.connect(self.open_bar_A)
        self._openbutton.setToolTip("Importe une nouvelle liste <b>A</b>")
        self.toolbar_A.addWidget(self._openbutton)
        # self._openbutton.setStyleSheet("color:red")

        self._savebuttonA = QToolButton()
        self._savebuttonA.setCheckable(False)
        self._savebuttonA.setChecked(False)
        self._savebuttonA.setAutoRaise(True)
        self._savebuttonA.setIcon(QtGui.QIcon("../icons/disketteA.png"))
        self._savebuttonA.setText("Save A")
        self._savebuttonA.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self._savebuttonA.clicked.connect(self.save_list_A)
        self.toolbar_A.addWidget(self._savebuttonA)

        self._delbuttonA = QToolButton()
        self._delbuttonA.setCheckable(False)
        self._delbuttonA.setChecked(False)
        self._delbuttonA.setAutoRaise(True)
        self._delbuttonA.setIcon(QtGui.QIcon("../icons/trashA.png"))
        self._delbuttonA.setText("Effacer A")
        self._delbuttonA.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self._delbuttonA.clicked.connect(self.del_list_A)
        self._delbuttonA.setToolTip("Efface la liste <b>A</b>")

        self.toolbar_A.addWidget(self._delbuttonA)

        # self.toolbar_A.addSeparator()

        self._openJsonbuttonA = QToolButton()
        # self._openJsonbuttonA.setMenu(self._menu)

        self._openJsonbuttonA.setCheckable(False)
        self._openJsonbuttonA.setChecked(False)
        self._openJsonbuttonA.setAutoRaise(True)
        self._openJsonbuttonA.setIcon(QtGui.QIcon("../icons/JsonA.png"))
        self._openJsonbuttonA.setText("A")
        self._openJsonbuttonA.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self._openJsonbuttonA.clicked.connect(self.open_json_A)
        self.toolbar_A.addWidget(self._openJsonbuttonA)

        self._delJsonbuttonA = QToolButton()
        self._delJsonbuttonA.setCheckable(False)
        self._delJsonbuttonA.setChecked(False)
        self._delJsonbuttonA.setAutoRaise(True)
        self._delJsonbuttonA.setIcon(QtGui.QIcon("../icons/x-markA.png"))
        self._delJsonbuttonA.setText("Del Json A")
        self._delJsonbuttonA.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self._delJsonbuttonA.clicked.connect(self.del_json_A)
        self.toolbar_A.addWidget(self._delJsonbuttonA)

        self._delJsonbuttonB = QToolButton()
        self._delJsonbuttonB.setCheckable(False)
        self._delJsonbuttonB.setChecked(False)
        self._delJsonbuttonB.setAutoRaise(True)
        self._delJsonbuttonB.setIcon(QtGui.QIcon("../icons/x-markB.png"))
        self._delJsonbuttonB.setText("Del Json B")
        self._delJsonbuttonB.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self._delJsonbuttonB.clicked.connect(self.del_json_B)
        self.toolbar_A.addWidget(self._delJsonbuttonB)

        self._openJsonbuttonB = QToolButton()
        self._openJsonbuttonB.setCheckable(False)
        self._openJsonbuttonB.setChecked(False)
        self._openJsonbuttonB.setAutoRaise(True)
        self._openJsonbuttonB.setIcon(QtGui.QIcon("../icons/JsonB.png"))
        self._openJsonbuttonB.setText("B")
        self._openJsonbuttonB.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self._openJsonbuttonB.clicked.connect(self.open_json_B)
        self.toolbar_A.addWidget(self._openJsonbuttonB)

        self._delbuttonB = QToolButton()
        self._delbuttonB.setCheckable(False)
        self._delbuttonB.setChecked(False)
        self._delbuttonB.setAutoRaise(True)
        self._delbuttonB.setIcon(QtGui.QIcon("../icons/trashB.png"))
        self._delbuttonB.setText("Effacer B")
        self._delbuttonB.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self._delbuttonB.clicked.connect(self.del_list_B)
        self._delbuttonB.setToolTip("Efface la liste <b>A</b>")

        self.toolbar_A.addWidget(self._delbuttonB)

        self._savebuttonB = QToolButton()
        self._savebuttonB.setCheckable(False)
        self._savebuttonB.setChecked(False)
        self._savebuttonB.setAutoRaise(True)
        self._savebuttonB.setIcon(QtGui.QIcon("../icons/disketteB.png"))
        self._savebuttonB.setText("Save B")
        self._savebuttonB.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self._savebuttonB.clicked.connect(self.save_list_B)
        self.toolbar_A.addWidget(self._savebuttonB)

        self._openbuttonB = QToolButton()
        self._openbuttonB.setCheckable(False)
        self._openbuttonB.setChecked(False)
        self._openbuttonB.setAutoRaise(True)
        self._openbuttonB.setIcon(QtGui.QIcon("../icons/ArrowB.png"))
        self._openbuttonB.setText("Open B")
        self._openbuttonB.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self._openbuttonB.clicked.connect(self.open_bar_B)
        self._openbuttonB.setToolTip("Importe une nouvelle liste <b>B</b>")

        self.toolbar_A.addWidget(self._openbuttonB)

    def open_bar_A(self):
        self.appli.init_list()

    def open_bar_B(self):
        self.appli.init_list_exclusion()

    def open_json_A(self):
        # self._openJsonbuttonA.showMenu()
        # return
        self.appli.load_json(self.appli.cb_import_json.currentText(), 'ref')

    def open_json_B(self):
        self.appli.load_json(self.appli.cb_import_json_exclusion.currentText(), 'excl')

    def save_list_A(self):
        pass

    def save_list_B(self):
        pass

    def del_list_A(self):
        self.appli.clear_list("A")

    def del_list_B(self):
        self.appli.clear_list("B")

    def del_json_A(self):
        self.appli.del_json(self.appli.cb_import_json.currentText())

    def del_json_B(self):
        self.appli.del_json(self.appli.cb_import_json_exclusion.currentText())


class Layer3V(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.layout3v = QtWidgets.QVBoxLayout()
        self.lw_lst1 =QtWidgets.QListWidget()
        self.lw_lst2 =QtWidgets.QListWidget()
        self.lw_lst3 =QtWidgets.QListWidget()
        self.lbl_1 = QtWidgets.QLabel("Liste 1")
        self.lbl_2 = QtWidgets.QLabel("Liste 2")
        self.lbl_3 = QtWidgets.QLabel("Liste 3")
        self.layout3v.addWidget(self.lbl_1)
        self.layout3v.addWidget(self.lw_lst1)
        self.layout3v.addWidget(self.lbl_2)
        self.layout3v.addWidget(self.lw_lst2)
        self.layout3v.addWidget(self.lbl_3)
        self.layout3v.addWidget(self.lw_lst3)

        self.setLayout(self.layout3v)


class MonLayerP(QtWidgets.QWidget):
    def __init__(self, w1, w2):
        super().__init__()
        self.w1 = w1
        self.w2 = w2
        self.setup_ui()

    def setup_ui(self):
        self.create_layouts()
        self.setLayout(self.main_layout)

    def create_layouts(self):
        self.main_layout = QtWidgets.QHBoxLayout()
        self.layout1 = QtWidgets.QVBoxLayout()
        self.layout2 = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.layout1)
        self.main_layout.addLayout(self.layout2)
        self.layout1.addWidget(self.w1)
        self.layout2.addWidget(self.w2)


class MainWindow(QtWidgets.QWidget):

    # def __init__(self, ctx):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        # self.ctx = ctx
        self.fichier = ""
        self.populate_widgets()
        self.nomfichier = ""
        self.fichier_ref = ""

    def setup_ui(self):

        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):

        self.btn_open_ref = QtWidgets.QPushButton("Importer Liste A")
        self.btn_open_exclusion = QtWidgets.QPushButton("Importer Liste B")
        self.cb_import_json = QtWidgets.QComboBox()
        self.cb_import_json_exclusion = QtWidgets.QComboBox()
        self.btn_load_json_ref = QtWidgets.QPushButton("Charger Json")
        self.btn_load_json_exclusion = QtWidgets.QPushButton("Charger Json")
        self.btn_del_json_ref = QtWidgets.QPushButton(QtGui.QIcon("../icons/dust-bin.png"), "")
        self.btn_del_json_exclusion = QtWidgets.QPushButton(QtGui.QIcon("../icons/dust-bin.png"), "")
        self.btn_convert_ref = QtWidgets.QPushButton("Sauvegarder")
        self.btn_convert_exclusion = QtWidgets.QPushButton("Sauvegarder")
        self.btn_text_ref = QtWidgets.QPushButton("Convertir texte")
        self.btn_text_exclusion = QtWidgets.QPushButton("Convertir texte")
        self.pt_texte_brut = QtWidgets.QTextEdit()
        self.le_adress_ref = QtWidgets.QLineEdit()
        self.le_adress_exclusion = QtWidgets.QLineEdit()
        self.lw_liste_ref = QtWidgets.QListWidget()
        self.lw_liste_exclusion = QtWidgets.QListWidget()
        self.lbl_ref_count = QtWidgets.QLabel()
        self.lbl_exclusion_count = QtWidgets.QLabel()
        self.btn_generate_list = QtWidgets.QPushButton("A-B")
        self.btn_add_list = QtWidgets.QPushButton("A+B")
        self.btn_diff_list = QtWidgets.QPushButton("X")
        self.btn_exclude = QtWidgets.QPushButton(QtGui.QIcon("../icons/next.png"), "")
        self.btn_include = QtWidgets.QPushButton(QtGui.QIcon("../icons/back.png"), "")
        self.btn_del_user = QtWidgets.QPushButton(QtGui.QIcon("../icons/user.png"), "")
        self.btn_clear_ref = QtWidgets.QPushButton("Effacer A")
        self.btn_clear_exclusion = QtWidgets.QPushButton("Effacer B")

        self.layerV = Layer3V()

    def modify_widgets(self):

        # css_file = self.ctx.get_resource("style.css")
        # with open(css_file, 'r') as f:
        #     self.setStyleSheet(f.read())

        self.lw_liste_ref.setSortingEnabled(True)
        self.lw_liste_exclusion.setSortingEnabled(True)
        self.setAcceptDrops(True)

        self.btn_text_ref.setEnabled(False)
        self.btn_text_exclusion.setEnabled(False)
        self.pt_texte_brut.setMaximumHeight(50)

        self.lw_liste_ref.setMinimumHeight(200)
        self.lw_liste_exclusion.setMinimumHeight(200)

        self.le_adress_exclusion.setPlaceholderText("Recherche")
        self.le_adress_ref.setPlaceholderText("Recherche")
        self.le_adress_exclusion.setEnabled(True)
        self.le_adress_ref.setEnabled(True)

        self.btn_generate_list.setFixedSize(50, 50)
        self.btn_add_list.setFixedSize(50, 50)
        self.btn_diff_list.setFixedSize(50, 50)

        self.btn_exclude.setFixedSize(50, 50)
        self.btn_include.setFixedSize(50, 50)
        self.btn_del_json_ref.setFixedSize(100, 50)
        self.btn_del_json_exclusion.setFixedSize(100, 50)
        self.btn_del_user.setFixedSize(50, 50)
        self.btn_load_json_ref.setFixedHeight(50)
        self.btn_load_json_exclusion.setFixedHeight(50)

        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(True)

        self.lbl_ref_count.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ref_count.setStyleSheet("background-color: rgb(155, 255, 143);")
        self.lbl_ref_count.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_ref_count.setText("0")
        self.lbl_ref_count.setFont(font)

        self.lbl_exclusion_count.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_exclusion_count.setStyleSheet("background-color: rgba(255, 95, 79, 135);")
        self.lbl_exclusion_count.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_exclusion_count.setText("0")
        self.lbl_exclusion_count.setFont(font)

        self.layerV.lbl_2.hide()
        self.layerV.lw_lst2.hide()
        self.layerV.lbl_3.hide()
        self.layerV.lw_lst3.hide()
        self.layerV.hide()

        self.layerV.lw_lst1.setFixedWidth(250)

        # QtWidgets.QToolTip.setFont(QtGui.QFont('Arial', 18))

        self.btn_del_user.setToolTip("Supprime la selection de la <b>liste A</b>")
        self.btn_diff_list.setToolTip("Renvoie la difference symetrique entre les 2 listes")
        self.btn_generate_list.setToolTip("Renvoie la liste <b>A</b> sans les elements de la liste <b>B</b>")
        self.btn_add_list.setToolTip("Renvoie la liste des éléments fusionnés de <b>A</b> et <b>B</b>")
        self.btn_exclude.setToolTip("Déplace la selection de la liste <b>A</b> vers la liste <b>B</b>")
        self.btn_include.setToolTip("Déplace la selection de la liste <b>B</b> vers la liste <b>A</b>")

    def create_layouts(self):
        self.layout_principal = QtWidgets.QHBoxLayout(self)
        self.main_layout = QtWidgets.QGridLayout()
        self.layout_resultats = QtWidgets.QVBoxLayout()
        self.layout_principal.addLayout(self.main_layout)
        self.layout_principal.addLayout(self.layout_resultats)


    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.btn_open_ref, 0, 0, 1, 2)
        self.main_layout.addWidget(self.btn_open_exclusion, 0, 3, 1, 2)
        self.main_layout.addWidget(self.cb_import_json, 1, 0, 1, 2)
        self.main_layout.addWidget(self.cb_import_json_exclusion, 1, 3, 1, 2)

        self.main_layout.addWidget(self.btn_load_json_ref, 2, 0, 1, 1)
        self.main_layout.addWidget(self.btn_del_json_ref, 2, 1, 1, 1)
        self.main_layout.addWidget(self.btn_del_json_exclusion, 2, 3, 1, 1)
        self.main_layout.addWidget(self.btn_load_json_exclusion, 2, 4, 1, 1)

        self.main_layout.addWidget(self.btn_text_ref, 3, 0, 1, 2)
        self.main_layout.addWidget(self.btn_text_exclusion, 3, 3, 1, 2)
        self.main_layout.addWidget(self.pt_texte_brut, 4, 0, 2, 5)

        self.main_layout.addWidget(self.le_adress_ref, 6, 0, 1, 1)
        self.main_layout.addWidget(self.btn_clear_ref, 6, 1, 1, 1)
        self.main_layout.addWidget(self.btn_clear_exclusion, 6, 3, 1, 1)
        self.main_layout.addWidget(self.le_adress_exclusion, 6, 4, 1, 1)

        self.main_layout.addWidget(self.lw_liste_ref, 7, 0, 4, 2)
        self.main_layout.addWidget(self.lw_liste_exclusion, 7, 3, 4, 2)
        self.main_layout.addWidget(self.lbl_ref_count, 11, 0, 2, 2)
        self.main_layout.addWidget(self.lbl_exclusion_count, 11, 3, 2, 2)

        self.main_layout.addWidget(self.btn_include, 7, 2, 1, 1)
        self.main_layout.addWidget(self.btn_exclude, 8, 2, 1, 1)
        self.main_layout.addWidget(self.btn_del_user, 6, 2, 1, 1)
        self.main_layout.addWidget(self.btn_diff_list, 9, 2, 1, 1)
        self.main_layout.addWidget(self.btn_generate_list, 10, 2, 1, 1)
        self.main_layout.addWidget(self.btn_add_list, 11, 2, 1, 1)

        self.layout_resultats.addWidget(self.layerV)

    def setup_connections(self):
        self.btn_open_ref.clicked.connect(self.init_list)
        self.btn_open_exclusion.clicked.connect(self.init_list_exclusion)
        self.btn_exclude.clicked.connect(self.delete_selected_ref)
        self.btn_include.clicked.connect(self.delete_selected_exclusion)
        self.btn_generate_list.clicked.connect(lambda: self.generate_list("exclude"))
        self.btn_add_list.clicked.connect(lambda: self.generate_list("add"))
        self.btn_diff_list.clicked.connect(lambda: self.generate_list("diff"))
        self.btn_load_json_ref.clicked.connect(lambda: self.load_json(self.cb_import_json.currentText(),
                                                                      'ref'))
        self.btn_load_json_exclusion.clicked.connect(lambda: self.load_json(self.cb_import_json_exclusion.currentText(),
                                                                            'excl'))
        self.btn_del_json_ref.clicked.connect(lambda: self.del_json(self.cb_import_json.currentText()))
        self.btn_del_json_exclusion.clicked.connect(lambda: self.del_json(self.cb_import_json_exclusion.currentText()))
        self.pt_texte_brut.textChanged.connect(self.enable_text)
        self.btn_text_ref.clicked.connect(self.convert_text)
        self.btn_text_exclusion.clicked.connect(self.convert_text_exclusion)
        self.le_adress_ref.textChanged.connect(lambda: self.search_ref("ref"))
        self.le_adress_exclusion.textChanged.connect(lambda: self.search_ref("exclusion"))
        self.btn_clear_ref.clicked.connect(lambda: self.clear_list("A"))
        self.btn_clear_exclusion.clicked.connect(lambda: self.clear_list("B"))
        self.btn_del_user.clicked.connect(self.del_user)

    def populate_widgets(self):
        self.populate_ref()
        self.populate_exclude()
        self.populate_cb_json()

    def populate_ref(self, nom_liste='last_ref'):
        self.lst_ref = Api.get_lst_from_json(nom_liste)
        self.lw_liste_ref.clear()
        if self.lst_ref or nom_liste == "last_ref":
            self.lw_liste_ref.addItems(self.lst_ref)
            self.lbl_ref_count.setText(str(len(self.lst_ref)))
        self.lw_liste_ref.repaint()
        Api.add_list_to_json(self.lst_ref, "last_ref")
        return

    def populate_exclude(self, nom_liste='last_exclusion'):
        self.lst_exclusion = Api.get_lst_from_json(nom_liste)
        self.lw_liste_exclusion.clear()
        if self.lst_exclusion or nom_liste == "last_exclusion":
            self.lw_liste_exclusion.addItems(self.lst_exclusion)
            self.lbl_exclusion_count.setText(str(len(self.lst_exclusion)))
        self.lw_liste_exclusion.repaint()
        Api.add_list_to_json(self.lst_exclusion, "last_exclusion")
        return

    def populate_cb_json(self):
        lst_json = Api.get_lst_of_json(Api.ADRESS_DIR)
        self.cb_import_json.clear()
        self.cb_import_json_exclusion.clear()
        self.cb_import_json.addItem("")
        self.cb_import_json_exclusion.addItem("")
        for key in lst_json:
            self.cb_import_json.addItem(key)
            self.cb_import_json_exclusion.addItem(key)
        return

    def open_file(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setMimeTypeFilters(["text/plain"])
        adress_dir = Api.ADRESS_DIR
        file_dialog.setDirectory(adress_dir)

        if file_dialog.exec_() == QtWidgets.QDialog.Accepted:
            return file_dialog.selectedFiles()[0]
        return False

    def init_list(self):
        """ ouvre un fichier texte contenant les adresses email au format outlook et appelle la fonction de convertion
        en liste"""

        self.fichier_ref = self.open_file()
        if self.fichier_ref:
            self.filename_ref = os.path.basename(self.fichier_ref[:-4])
        else:
            logging.info("L'ouverture du fichier a échoué")
            return

        with open(self.fichier_ref, 'r', encoding='ISO-8859-1') as f:
            logging.info(f'ouverture du fichier {self.filename_ref}')
            txt = f.read().strip()
        self.convert_to_list(txt)
        return

    def convert_to_list(self, txt):
        """ appelle la fonction de convertion de texte en liste et affiche la liste dans le widget lw_liste_ref"""
        # self.lst_ref = api.txt_to_lst(self.fichier_ref)
        self.lst_ref = Api.txt_to_lst(txt)
        # liste1 = api.txt_to_lst(txt)
        self.lw_liste_ref.clear()
        # logging.debug("La liste a été effacée")
        for item in self.lst_ref:
            self.lw_liste_ref.addItem(item)
        self.lw_liste_ref.repaint()
        self.lbl_ref_count.setText(str(len(self.lst_ref)))
        # self.lbl_ref_count.setText(str(len(liste1)))

        Api.save_json(lst=self.lst_ref, nom_fichier='lst_ref')
        Api.save_json(lst=self.lst_ref, nom_fichier='last_ref')
        self.btn_convert_ref.setEnabled(True)

        return

    def init_list_exclusion(self):
        self.fichier = self.open_file()
        if not self.fichier:
            return
        self.filename_exclusion = os.path.basename(self.fichier[:-4])
        # if self.fichier_exclusion:
        #     self.filename_ref = os.path.basename(self.fichier_exclusion[:-4])
        # else:
        #     logging.info("L'ouverture du fichier a échoué")
        #     return

        with open(self.fichier, 'r', encoding='ISO-8859-1') as f:
            logging.info(f'ouverture du fichier {self.filename_exclusion}')
            txt = f.read().strip()
        self.convert_txt_to_lst_exclusion(txt)
        return

    def convert_txt_to_lst_exclusion(self, txt):
        """converti le texte en liste"""
        # self.lst_exclusion = api.txt_to_lst(self.fichier)
        self.lst_exclusion = Api.txt_to_lst(txt)
        self.lw_liste_exclusion.clear()
        # logging.info("la liste exclusion a été effacée")
        for item in self.lst_exclusion:
            self.lw_liste_exclusion.addItem(item)
        self.lw_liste_exclusion.repaint()
        self.lbl_exclusion_count.setText(str(len(self.lst_exclusion)))
        # api.save_json(lst=self.lst_exclusion, nom_liste='lst_exclusion')
        Api.save_json(lst=self.lst_exclusion, nom_fichier='lst_exclusion')
        Api.save_json(lst=self.lst_exclusion, nom_fichier='last_exclusion')
        return

    def save_ref_to_json(self):
        if self.filename_ref:
            Api.save_json(self.lst_ref, self.filename_ref)

    def save_exclusion_to_json(self):
        path = os.path.basename(self.filename_exclusion)[:-5]
        # logging.info(path)
        Api.save_json(self.lst_exclusion, path)

    def get_selected_item_ref(self):
        selected_items = self.lw_liste_ref.selectedItems()
        if selected_items:
            return selected_items[0]
        return None

    def get_selected_item_exclude(self):
        selected_items = self.lw_liste_exclusion.selectedItems()
        if selected_items:
            return selected_items[0]
        return None

    def delete_selected_ref(self):
        self.flag_ref = False
        selected_item = self.get_selected_item_ref()

        if selected_item:
            resultat = True
            if resultat:
                self.lw_liste_ref.takeItem(self.lw_liste_ref.row(selected_item))
                self.lst_ref.remove(selected_item.text())
                self.lbl_ref_count.setText(str(len(self.lst_ref)))
                # api.save_json(lst=self.lst_ref, nom_fichier='lst_ref')
                Api.save_json(lst=self.lst_ref, nom_fichier='last_ref')

                if selected_item.text() not in self.lst_exclusion:
                    self.lst_exclusion.append(selected_item.text())
                    self.lbl_exclusion_count.setText(str(len(self.lst_exclusion)))
                    # api.save_json(lst=self.lst_exclusion, nom_fichier='lst_exclusion')
                    Api.save_json(lst=self.lst_exclusion, nom_fichier='last_exclusion')
                else:
                    self.flag = True

            self.populate_ref()
            self.populate_exclude()

    def delete_selected_exclusion(self):
        self.flag_exclude = False
        selected_item = self.get_selected_item_exclude()

        if selected_item:
            resultat = True
            if resultat:
                self.lw_liste_exclusion.takeItem(self.lw_liste_exclusion.row(selected_item))
                self.lst_exclusion.remove(selected_item.text())
                self.lbl_exclusion_count.setText(str(len(self.lst_exclusion)))
                # api.save_json(lst=self.lst_exclusion, nom_fichier='lst_exclusion')
                Api.save_json(lst=self.lst_exclusion, nom_fichier='last_exclusion')
                if selected_item.text() not in self.lst_ref:
                    self.lst_ref.append(selected_item.text())
                    self.lbl_ref_count.setText(str(len(self.lst_ref)))
                    # api.save_json(lst=self.lst_ref, nom_fichier='lst_ref')
                    Api.save_json(lst=self.lst_ref, nom_fichier='last_ref')
                else:
                    self.flag = True

            self.populate_ref()
            self.populate_exclude()

    def generate_list(self, func):

        boite = QtWidgets.QMessageBox.question(self, 'Sauvegarde', 'Liste à réutiliser ?')
        if boite == QtWidgets.QMessageBox.StandardButton.Yes:
            text, ok = QtWidgets.QInputDialog.getText(self, 'Nom de liste', 'Donnez un nom à cette liste')
            nom_liste = text

        else:
            nom_liste = None
        self.layerV.show()
        lst_filtre = []
        if func == "exclude":
            lst_filtre = Api.process(lst_origine=self.lst_ref, lst_exclusion=self.lst_exclusion)
            lst_filtre.sort()
            self.layerV.lbl_2.hide()
            self.layerV.lbl_3.hide()
            self.layerV.lw_lst2.hide()
            self.layerV.lw_lst3.hide()
        elif func == "add":
            lst_filtre = Api.add_list(self.lst_ref, self.lst_exclusion)
            lst_filtre.sort()
            self.layerV.lbl_2.hide()
            self.layerV.lbl_3.hide()
            self.layerV.lw_lst2.hide()
            self.layerV.lw_lst3.hide()
        elif func == "diff":
            lst_filtre = Api.list_ecart(self.lst_ref, self.lst_exclusion)
            lst_A = Api.process(self.lst_ref, self.lst_exclusion)
            lst_B = Api.process(self.lst_exclusion, self.lst_ref)
            self.layerV.lbl_2.setText("Dans A pas dans B")
            self.layerV.lbl_3.setText("Dans B pas dans A")
            self.layerV.lw_lst2.addItems(lst_A)
            self.layerV.lw_lst3.addItems(lst_B)
            self.layerV.lbl_2.show()
            self.layerV.lbl_3.show()
            self.layerV.lw_lst2.show()
            self.layerV.lw_lst3.show()

            lst_filtre.sort()

        self.layerV.lbl_1.setText("Resultats")
        self.layerV.lw_lst1.addItems(lst_filtre)

        if nom_liste:
            Api.add_list_to_json(lst_filtre, nom=nom_liste)
            logging.info(f"la liste {nom_liste} a été rajouté au fichier JSON")
            self.populate_cb_json()

        result = self.save_result(lst_filtre)

        # if self.fichier_ref:
        #     nom_fichier_filtre = f"{os.path.splitext(self.fichier_ref)[0]}" \
        #                          f"_{func}{os.path.splitext(self.fichier_ref)[1]}"
        # else:
        #     file_dialog = QtWidgets.QFileDialog(self)
        #     file_dialog.setViewMode(QtWidgets.QFileDialog.Detail)
        #     nom_fichier_filtre = file_dialog.getSaveFileName(self)[0]
        #     if not nom_fichier_filtre:
        #         return
        #         # t = datetime.now()
        #         # nom_fichier_filtre = str(t.date())+"-"+str(t.time())[:-7]
        #
        # result = Api.write_to_disk(path=os.path.join(Api.ADRESS_DIR, nom_fichier_filtre), lst=lst_filtre)
        # result = True
        # if result:
        #     message_box = QtWidgets.QMessageBox()
        #     message_box.setWindowTitle("Process")
        #     message_box.setText(f"Le fichier {os.path.basename(nom_fichier_filtre)}"
        #                         f" contenant {len(lst_filtre)} adresses a été créé dans le"
        #                         f" dossier {Api.ADRESS_DIR}")
        #     message_box.exec_()
        return result

    def save_result(self, liste):

        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setViewMode(QtWidgets.QFileDialog.Detail)
        nom_fichier_filtre = file_dialog.getSaveFileName(self)[0]
        nom_dir = file_dialog.directory().path()
        if not nom_fichier_filtre:
            return
            # t = datetime.now()
            # nom_fichier_filtre = str(t.date())+"-"+str(t.time())[:-7]
        # result = True
        result = Api.write_to_disk(path=os.path.join(Api.RESULT_DIR, nom_fichier_filtre), lst=liste)
        if result:
            message_box = QtWidgets.QMessageBox()
            message_box.setWindowTitle("Process")
            message_box.setText(f"Le fichier {os.path.basename(nom_fichier_filtre)}"
                                f" contenant {len(liste)} adresses a été créé dans le"
                                f" dossier {nom_dir}")
            message_box.exec_()
        return result

    def load_json(self, nom_lst, cb):
        if nom_lst:
            logging.debug(f"la liste {nom_lst} va être chargée")
            self.layerV.lbl_2.hide()
            self.layerV.lbl_3.hide()
            self.layerV.lw_lst2.hide()
            self.layerV.lw_lst3.hide()
            self.layerV.lw_lst1.clear()
            if cb == "ref":
                self.populate_ref(nom_liste=nom_lst)
                self.le_adress_ref.repaint()
                self.cb_import_json.setCurrentIndex(0)
            else:
                self.populate_exclude(nom_liste=nom_lst)
                self.le_adress_exclusion.repaint()
                self.cb_import_json_exclusion.setCurrentIndex(0)
        else:
            logging.error("aucune liste sélectionnée")
            return

        self.cb_import_json.setCurrentIndex(0)
        self.cb_import_json_exclusion.setCurrentIndex(0)
        self.cb_import_json.repaint()
        self.cb_import_json_exclusion.repaint()
        return

    def del_json(self, nom_lst):
        if nom_lst:
            reponse = QtWidgets.QMessageBox.question(self, "Suppression", f"Voulez vous supprimer la liste {nom_lst}")
        else:
            return

        if reponse == QtWidgets.QMessageBox.StandardButton.Yes:
            Api.remove_list_from_json(nom_lst)
            logging.info(f"La liste {nom_lst} a été supprimée")
            self.populate_cb_json()

        self.cb_import_json.setCurrentIndex(0)
        self.cb_import_json_exclusion.setCurrentIndex(0)

        return

    def del_user(self):
        if self.lw_liste_ref.selectedItems():
            for item in self.lw_liste_ref.selectedItems():
                print(item.text())
                self.lw_liste_ref.takeItem(self.lw_liste_ref.row(item))
                self.lst_ref.remove(item.text())
                Api.add_list_to_json(self.lst_ref, nom="last_ref")
                self.populate_ref()
        else:
            print("NOK")

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        event.accept()
        self.pt_texte_brut.setText(event.mimeData().data('text'))

    def enable_text(self):
        self.btn_text_ref.setEnabled(True)
        self.btn_text_exclusion.setEnabled(True)

    def convert_text(self):
        txt = self.pt_texte_brut.toPlainText()
        # texte_valide = re.search(r'([A-Z ]+[a-zA-Z]+ <.+@rte-france\.com>; )', txt)
        texte_valide = re.search(r'.', txt)
        if not texte_valide:
            return
        # self.convert_to_list(texte_valide.group())
        self.convert_to_list(txt)
        self.pt_texte_brut.clear()
        self.btn_text_ref.setEnabled(False)
        self.btn_text_exclusion.setEnabled(False)

    def convert_text_exclusion(self):
        txt = self.pt_texte_brut.toPlainText()
        texte_valide = re.search(r'([A-Z ]+[a-zA-Z]+ <.+@rte-france\.com>; )', txt)
        if not texte_valide:
            return
        self.convert_txt_to_lst_exclusion(texte_valide.group())
        self.pt_texte_brut.clear()
        self.btn_text_exclusion.setEnabled(False)
        self.btn_text_ref.setEnabled(False)

    def search_ref(self, lste):
        if lste == "ref":
            self.lw_liste_ref.clear()
            self.populate_ref()
            items = self.lw_liste_ref.findItems(self.le_adress_ref.text(), QtCore.Qt.MatchContains)

        else:
            self.lw_liste_exclusion.clear()
            self.populate_exclude()
            items = self.lw_liste_exclusion.findItems(self.le_adress_exclusion.text(), QtCore.Qt.MatchContains)

        lst = [item.text() for item in items]

        if lste == "ref":
            self.lw_liste_ref.clear()
            self.lw_liste_ref.addItems(lst)
            self.lbl_ref_count.setText(str(len(lst)))
        else:
            self.lw_liste_exclusion.clear()
            self.lw_liste_exclusion.addItems(lst)
            self.lbl_exclusion_count.setText(str(len(lst)))

    def clear_list(self, lw):
        lst = []
        if lw == "A":
            self.lw_liste_ref.clear()
            Api.add_list_to_json(lst, "last_ref")
            self.populate_ref(nom_liste="last_ref")
            self.lw_liste_ref.repaint()
        else:
            self.lw_liste_exclusion.clear()
            Api.add_list_to_json(lst, "last_exclusion")
            self.populate_exclude(nom_liste="last_exclusion")
            self.lw_liste_exclusion.repaint()
        return


if __name__ == '__main__':
    pass



