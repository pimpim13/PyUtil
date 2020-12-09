from PySide2 import QtWidgets, QtCore, QtGui
import package.API.Adress as api
import os
import re
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)


class MainWindow(QtWidgets.QWidget):

    def __init__(self, ctx):
        super().__init__()
        self.setup_ui()
        self.ctx = ctx
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
        self.btn_generate_list = QtWidgets.QPushButton("Générer liste A-B")
        self.btn_add_list = QtWidgets.QPushButton("Union des listes A+B")
        self.btn_exclude = QtWidgets.QPushButton(QtGui.QIcon("../icons/next.png"), "")
        self.btn_include = QtWidgets.QPushButton(QtGui.QIcon("../icons/back.png"), "")
        self.btn_del_user = QtWidgets.QPushButton(QtGui.QIcon("../icons/user.png"), "")
        self.btn_clear_ref = QtWidgets.QPushButton("Effacer A")
        self.btn_clear_exclusion = QtWidgets.QPushButton("Effacer B")



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

        self.btn_generate_list.setMinimumHeight(50)
        self.btn_add_list.setMinimumHeight(50)

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

        self.btn_del_user.setToolTip("Supprime la selection de la liste A")

    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout(self)

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

        self.main_layout.addWidget(self.lw_liste_ref, 7, 0, 3, 2)
        self.main_layout.addWidget(self.lw_liste_exclusion, 7, 3, 3, 2)
        self.main_layout.addWidget(self.lbl_ref_count, 11, 0, 2, 2)
        self.main_layout.addWidget(self.lbl_exclusion_count, 11, 3, 2, 2)
        self.main_layout.addWidget(self.btn_generate_list, 14, 0, 2, 2)
        self.main_layout.addWidget(self.btn_add_list, 14, 3, 2, 2)
        self.main_layout.addWidget(self.btn_include, 7, 2, 1, 1)
        self.main_layout.addWidget(self.btn_exclude, 8, 2, 1, 1)
        self.main_layout.addWidget(self.btn_del_user, 9, 2, 2, 1)

    def setup_connections(self):
        self.btn_open_ref.clicked.connect(self.init_list)
        self.btn_open_exclusion.clicked.connect(self.init_list_exclusion)
        self.btn_exclude.clicked.connect(self.delete_selected_ref)
        self.btn_include.clicked.connect(self.delete_selected_exclusion)
        self.btn_generate_list.clicked.connect(lambda: self.generate_list("exclude"))
        self.btn_add_list.clicked.connect(lambda: self.generate_list("add"))
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
        self.lst_ref = api.get_lst_from_json(nom_liste)
        self.lw_liste_ref.clear()
        if self.lst_ref or nom_liste == "last_ref":
            self.lw_liste_ref.addItems(self.lst_ref)
            self.lbl_ref_count.setText(str(len(self.lst_ref)))
        self.lw_liste_ref.repaint()
        api.add_list_to_json(self.lst_ref, "last_ref")
        return

    def populate_exclude(self, nom_liste='last_exclusion'):
        self.lst_exclusion = api.get_lst_from_json(nom_liste)
        self.lw_liste_exclusion.clear()
        if self.lst_exclusion or nom_liste == "last_exclusion":
            self.lw_liste_exclusion.addItems(self.lst_exclusion)
            self.lbl_exclusion_count.setText(str(len(self.lst_exclusion)))
        self.lw_liste_exclusion.repaint()
        api.add_list_to_json(self.lst_exclusion, "last_exclusion")
        return

    def populate_cb_json(self):
        lst_json = api.get_lst_of_json(api.ADRESS_DIR)
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
        adress_dir = api.ADRESS_DIR
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

    def convert_to_list(self, txt):
        """ appelle la fonction de convertion de texte en liste et affiche la liste dans le widget lw_liste_ref"""
        # self.lst_ref = api.txt_to_lst(self.fichier_ref)
        self.lst_ref = api.txt_to_lst(txt)
        # liste1 = api.txt_to_lst(txt)
        self.lw_liste_ref.clear()
        # logging.debug("La liste a été effacée")
        for item in self.lst_ref:
            self.lw_liste_ref.addItem(item)
        self.lw_liste_ref.repaint()
        self.lbl_ref_count.setText(str(len(self.lst_ref)))
        # self.lbl_ref_count.setText(str(len(liste1)))

        api.save_json(lst=self.lst_ref, nom_fichier='lst_ref')
        api.save_json(lst=self.lst_ref, nom_fichier='last_ref')
        self.btn_convert_ref.setEnabled(True)

        return

    def init_list_exclusion(self):
        self.fichier = self.open_file()
        self.filename_exclusion = os.path.basename(self.fichier[:-4])

        with open(self.fichier, 'r', encoding='ISO-8859-1') as f:
            # logging.info(f'ouverture du fichier {self.filename_exclusion}')
            txt = f.read().strip()

        self.convert_txt_to_lst_exclusion(txt)

    def convert_txt_to_lst_exclusion(self, txt):
        """converti le texte en liste"""
        # self.lst_exclusion = api.txt_to_lst(self.fichier)
        self.lst_exclusion = api.txt_to_lst(txt)
        self.lw_liste_exclusion.clear()
        # logging.info("la liste exclusion a été effacée")
        for item in self.lst_exclusion:
            self.lw_liste_exclusion.addItem(item)
        self.lw_liste_exclusion.repaint()
        self.lbl_exclusion_count.setText(str(len(self.lst_exclusion)))
        # api.save_json(lst=self.lst_exclusion, nom_liste='lst_exclusion')
        api.save_json(lst=self.lst_exclusion, nom_fichier='lst_exclusion')
        api.save_json(lst=self.lst_exclusion, nom_fichier='last_exclusion')
        return

    def save_ref_to_json(self):
        if self.filename_ref:
            api.save_json(self.lst_ref, self.filename_ref)

    def save_exclusion_to_json(self):
        path = os.path.basename(self.filename_exclusion)[:-5]
        # logging.info(path)
        api.save_json(self.lst_exclusion, path)

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
                api.save_json(lst=self.lst_ref, nom_fichier='last_ref')

                if selected_item.text() not in self.lst_exclusion:
                    self.lst_exclusion.append(selected_item.text())
                    self.lbl_exclusion_count.setText(str(len(self.lst_exclusion)))
                    # api.save_json(lst=self.lst_exclusion, nom_fichier='lst_exclusion')
                    api.save_json(lst=self.lst_exclusion, nom_fichier='last_exclusion')
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
                api.save_json(lst=self.lst_exclusion, nom_fichier='last_exclusion')
                if selected_item.text() not in self.lst_ref:
                    self.lst_ref.append(selected_item.text())
                    self.lbl_ref_count.setText(str(len(self.lst_ref)))
                    # api.save_json(lst=self.lst_ref, nom_fichier='lst_ref')
                    api.save_json(lst=self.lst_ref, nom_fichier='last_ref')
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

        lst_filtre = []
        if func == "exclude":
            lst_filtre = api.process(lst_origine=self.lst_ref, lst_exclusion=self.lst_exclusion)
            lst_filtre.sort()
        elif func == "add":
            lst_filtre = api.add_list(self.lst_ref, self.lst_exclusion)
            lst_filtre.sort()

        if nom_liste:
            api.add_list_to_json(lst_filtre, nom=nom_liste)
            logging.info(f"la liste {nom_liste} a été rajouté au fichier JSON")
            self.populate_cb_json()

        if self.fichier_ref:
            nom_fichier_filtre = f"{os.path.splitext(self.fichier_ref)[0]}" \
                                 f"_{func}{os.path.splitext(self.fichier_ref)[1]}"
        else:
            file_dialog = QtWidgets.QFileDialog(self)
            nom_fichier_filtre = file_dialog.getSaveFileName(self)[0]
            if not nom_fichier_filtre:
                t = datetime.now()
                nom_fichier_filtre = str(t.date())+"-"+str(t.time())[:-7]

        result = api.write_to_disk(path=os.path.join(api.ADRESS_DIR, nom_fichier_filtre), lst=lst_filtre)
        # result = True
        if result:
            message_box = QtWidgets.QMessageBox()
            message_box.setWindowTitle("Process")
            message_box.setText(f"Le fichier {os.path.basename(nom_fichier_filtre)}"
                                f" contenant {len(lst_filtre)} adresses a été créé dans le"
                                f" dossier {api.ADRESS_DIR}")
            message_box.exec_()
        return result

    def load_json(self, nom_lst, cb):
        if nom_lst:
            logging.debug(f"la liste {nom_lst} va être chargée")
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
            api.remove_list_from_json(nom_lst)
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
                api.add_list_to_json(self.lst_ref, nom="last_ref")
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
            api.add_list_to_json(lst, "last_ref")
            self.populate_ref(nom_liste="last_ref")
            self.lw_liste_ref.repaint()
        else:
            self.lw_liste_exclusion.clear()
            api.add_list_to_json(lst, "last_exclusion")
            self.populate_exclude(nom_liste="last_exclusion")
            self.lw_liste_exclusion.repaint()
        return



if __name__ == '__main__':
    print(os.curdir)