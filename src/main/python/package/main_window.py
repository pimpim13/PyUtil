from PySide2 import QtWidgets, QtCore, QtGui
import package.API.Adress as api
from Adress4_UI import Ui_Form
import os
import re
import logging

logging.basicConfig(level=logging.DEBUG)


class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, ctx):
        super().__init__()
        # self.setup_ui(self)
        self.ctx = ctx
        self.setupUi(self)
        self.fichier = ""
        self.modify_widgets()
        self.setup_connections()

        self.populate_widgets()

    def modify_widgets(self):

        # css_file = self.ctx.get_resource("style.css")
        # with open(css_file, 'r') as f:
        #     self.setStyleSheet(f.read())

        self.lw_liste_ref.setSortingEnabled(True)
        self.lw_liste_exclusion.setSortingEnabled(True)
        self.setAcceptDrops(True)
        # self.lbl_dropinfo.setVisible(False)
        self.btn_convert_ref.setEnabled(False)
        self.btn_text_ref.setEnabled(False)
        self.btn_text_exclusion.setEnabled(False)

    def setup_connections(self):
        self.btn_open_ref.clicked.connect(self.init_list)
        self.btn_open_exclusion.clicked.connect(self.init_list_exclusion)
        self.btn_convert_ref.clicked.connect(self.save_ref_to_json)
        self.btn_convert_exclusion.clicked.connect(self.save_exclusion_to_json)
        self.btn_exclude.clicked.connect(self.exclude_from_ref)
        self.btn_include.clicked.connect(self.exclude_from_exclusion)
        self.btn_generate_list.clicked.connect(self.generate_list)
        self.cb_import_json.currentIndexChanged.connect(self.load_json)
        self.pt_texte_brut.textChanged.connect(self.enable_text)
        self.btn_text_ref.clicked.connect(self.convert_text)
        self.btn_text_exclusion.clicked.connect(self.convert_text_exclusion)

    def open_file(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setMimeTypeFilters(["text/plain"])
        # adress_dir = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.HomeLocation)
        adress_dir = api.ADRESS_DIR
        file_dialog.setDirectory(adress_dir)
        if file_dialog.exec_() == QtWidgets.QDialog.Accepted:
            adress = file_dialog.selectedFiles()[0]
            return adress

    def init_list(self):
        self.fichier_ref = self.open_file()
        if self.fichier_ref:
            self.filename_ref = os.path.basename(self.fichier_ref[:-4])
        else:
            return

        with open(self.fichier_ref, 'r', encoding='ISO-8859-1') as f:
            logging.info(f'ouverture du fichier {self.filename_ref}')
            txt = f.read().strip()
        self.convert_to_list(txt)

    def convert_to_list(self, txt):
        # self.lst_ref = api.txt_to_lst(self.fichier_ref)
        self.lst_ref = api.txt_to_lst(txt)
        self.lw_liste_ref.clear()
        logging.debug("La liste a été effacée")
        for item in self.lst_ref:
            self.lw_liste_ref.addItem(item)
        self.lw_liste_ref.repaint()
        self.lbl_ref_count.setText(str(len(self.lst_ref)))

        api.save_json(lst=self.lst_ref, nom_fichier='lst_ref')
        self.btn_convert_ref.setEnabled(True)

        return

    def init_list_exclusion(self):
        self.fichier = self.open_file()
        self.filename_exclusion = os.path.basename(self.fichier[:-4])

        with open(self.fichier, 'r', encoding='ISO-8859-1') as f:
            logging.info(f'ouverture du fichier {self.filename_exclusion}')
            txt = f.read().strip()

        self.convert_txt_to_lst_exclusion(txt)

    def convert_txt_to_lst_exclusion(self, txt):
        "converti le texte en liste"
        # self.lst_exclusion = api.txt_to_lst(self.fichier)
        self.lst_exclusion = api.txt_to_lst(txt)
        self.lw_liste_exclusion.clear()
        logging.info("la liste exclusion a été effacée")
        for item in self.lst_exclusion:
            self.lw_liste_exclusion.addItem(item)
        self.lw_liste_exclusion.repaint()
        self.lbl_exclusion_count.setText(str(len(self.lst_exclusion)))
        # api.save_json(lst=self.lst_exclusion, nom_liste='lst_exclusion')
        api.save_json(lst=self.lst_exclusion, nom_fichier='lst_exclusion')
        return

    def save_ref_to_json(self):
        if self.filename_ref:
            api.save_json(self.lst_ref, self.filename_ref)

    def save_exclusion_to_json(self):
        path = os.path.basename(self.filename_exclusion)[:-5]
        print(path)
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
                api.save_json(lst=self.lst_ref, nom_fichier='lst_ref')
                if selected_item.text() not in self.lst_exclusion:
                    self.lst_exclusion.append(selected_item.text())
                    self.lbl_exclusion_count.setText(str(len(self.lst_exclusion)))
                    api.save_json(lst=self.lst_exclusion, nom_fichier='lst_exclusion')
                else:
                    self.flag = True

    def delete_selected_exclusion(self):
        self.flag_exclude = False
        selected_item = self.get_selected_item_exclude()

        if selected_item:
            resultat = True
            if resultat:
                self.lw_liste_exclusion.takeItem(self.lw_liste_exclusion.row(selected_item))
                self.lst_exclusion.remove(selected_item.text())
                self.lbl_exclusion_count.setText(str(len(self.lst_exclusion)))
                api.save_json(lst=self.lst_exclusion, nom_fichier='lst_exclusion')
                if selected_item.text() not in self.lst_ref:
                    self.lst_ref.append(selected_item.text())
                    self.lbl_ref_count.setText(str(len(self.lst_ref)))
                    api.save_json(lst=self.lst_ref, nom_fichier='lst_exclusion')
                else:
                    self.flag = True

    def exclude_from_ref(self):

        self.delete_selected_ref()
        self.lw_liste_ref.repaint()
        if not self.flag_ref:
            if not self.lw_liste_exclusion.findItems(self.lst_exclusion[-1], QtCore.Qt.MatchExactly ):
                self.lw_liste_exclusion.addItem(self.lst_exclusion[-1])
                self.lw_liste_exclusion.repaint()
            else:
                logging.info("L'adresse email est déjà dans la liste")

    def exclude_from_exclusion(self):

        self.delete_selected_exclusion()
        self.lw_liste_exclusion.repaint()
        if not self.flag_exclude:
            if not self.lw_liste_ref.findItems(self.lst_ref[-1], QtCore.Qt.MatchExactly ):
                self.lw_liste_ref.addItem(self.lst_ref[-1])
                self.lw_liste_ref.repaint()
            else:
                logging.info("L'entrée est déjà dans la liste")

    def generate_list(self):

        lst_filtre = api.process(lst_origine=self.lst_ref, lst_exclusion=self.lst_exclusion)
        lst_filtre.sort()
        result = api.write_to_disk(path=os.path.join(api.ADRESS_DIR, 'lst_ref_filtre'), lst=lst_filtre)
        if result:
            message_box = QtWidgets.QMessageBox()
            message_box.setWindowTitle("Process")
            message_box.setText(f"Le fichier lst_ref_filtre contenant {len(lst_filtre)} adresses a été créé dans le"
                                f" dossier {api.ADRESS_DIR}" )
            message_box.exec_()
        return result

    def populate_widgets(self):

        self.populate_ref()
        self.populate_exclude()
        self.populate_cb_json()
        return

    def populate_ref(self):
        path = os.path.join(api.ADRESS_DIR, 'lst_ref.json')
        self.lst_ref = api.get_lst_from_json(path=path, nom_liste='lst_ref')
        if self.lst_ref:
            # for item in self.lst_ref:
            #     self.lw_liste_ref.addItem(item)
            self.lw_liste_ref.addItems(self.lst_ref)
            self.lw_liste_ref.repaint()
            self.lbl_ref_count.setText(str(len(self.lst_ref)))

    def populate_exclude(self):
        path = os.path.join(api.ADRESS_DIR, 'lst_exclusion.json')
        self.lst_exclusion = api.get_lst_from_json(path=path, nom_liste='lst_exclusion')
        if self.lst_exclusion:
            self.lw_liste_exclusion.addItems(self.lst_exclusion)
            self.lw_liste_exclusion.repaint()
            self.filename_exclusion = path
            self.lbl_exclusion_count.setText(str(len(self.lst_exclusion)))
        return

    def populate_cb_json(self):
        lst_json = api.get_lst_of_json(api.ADRESS_DIR)
        lst = [os.path.basename(item)[:-5] for item in lst_json]
        lst.insert(0, "")
        self.cb_import_json.addItems(lst)

    def load_json(self):
        """ à voir si on conserve """
        filename = self.cb_import_json.currentText()
        if os.path.exists(f'{api.ADRESS_DIR}/{filename}.json'):
            print(f'{api.ADRESS_DIR}/{filename}.json')
        return

    def dragEnterEvent(self, event):
        event.accept()

    # def dragLeaveEvent(self, event):
    #     pass

    def dropEvent(self, event):
        event.accept()
        # for url in event.mimeData().urls():
        #     self.add_file(path=url.toLocalFile())
        self.pt_texte_brut.setText(event.mimeData().data())

    def enable_text(self):
        self.btn_text_ref.setEnabled(True)
        self.btn_text_exclusion.setEnabled(True)

    def convert_text(self):
        txt = self.pt_texte_brut.toPlainText()
        texte_valide = re.search(r'[A-Z ]+[a-zA-Z]+ <.+@rte-france\.com>;\s*', txt)
        self.convert_to_list(texte_valide.group())
        self.pt_texte_brut.clear()
        self.btn_text_ref.setEnabled(False)
        self.btn_text_exclusion.setEnabled(False)

    def convert_text_exclusion(self):
        txt = self.pt_texte_brut.toPlainText()
        texte_valide = re.search(r'[A-Z ]+[a-zA-Z]+ <.+@rte-france\.com>;\s*', txt)
        self.convert_txt_to_lst_exclusion(texte_valide.group())
        self.pt_texte_brut.clear()
        self.btn_text_exclusion.setEnabled(False)
        self.btn_text_ref.setEnabled(False)
