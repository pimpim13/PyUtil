# -*- coding: utf-8 -*-
import json
import logging
import os
import re
import sys
from datetime import datetime
from pathlib import Path

niveau = logging.DEBUG

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='test_log.log', level=niveau,
                    format='%(asctime)s -- %(funcName)s -- %(name)s -- %(levelname)s -- %(message)s')
path_appli = os.path.dirname(__file__)

if not os.path.exists('setup.json'):
    setup_file = {"ADRESS_DIR": 'adress', "FILE_NAME": 'lst_ref.json', "RESULT_DIR": 'resultats'}
    with open('setup.json', 'w') as f:
        json.dump(setup_file, f, indent=4)
        logging.info('création du fichier de setup')

    logging.debug("le fichier de setup a été créé")

with open('setup.json', 'r') as f:
    setup_file = json.load(f)

if sys.platform == 'win32':
    ADRESS_DIR = f'D{os.path.join(Path.home(), setup_file["ADRESS_DIR"])[1:]}'
    RESULT_DIR = f'D{os.path.join(Path.home(), setup_file["ADRESS_DIR"], setup_file["RESULT_DIR"])[1:]}'
else:
    ADRESS_DIR = os.path.join(Path.home(), setup_file["ADRESS_DIR"])  # le dossier de travail est dans le dossier user
    RESULT_DIR = os.path.join(Path.home(), setup_file["ADRESS_DIR"], setup_file["RESULT_DIR"])

FILE_NAME = setup_file["FILE_NAME"]  # récupère le nom du fichier de données dans le fichier setup

path = os.path.join(ADRESS_DIR, FILE_NAME)

if not os.path.exists(path):
    logging.error(f"Le fichier {path} n'existe pas ")
    init = {"last_ref": [], "last_exclusion": []}
    with open(path, 'w') as f:
        json.dump(init, f, indent=4)
    logging.info('création du fichier de données')


def txt_to_lst(text=""):

    lst = re.split(r'[<> ;]', text)
    # lst = re.split(r'<|>| |;', text)
    lst = [item for item in lst if '@' in item and '--' not in item]

    return list(set(lst))


def write_to_disk(path, lst):
    """ Fonction qui écrit à l'adresse path le fichier texte passé en parametre
    """
    p = os.path.dirname(path)
    b = os.path.basename(path)
    t = os.path.splitext(b)
    name = os.path.join(os.path.dirname(path), f'{t[0]}.txt')

    if not os.path.exists(RESULT_DIR):
        os.makedirs(RESULT_DIR)

    with open(name, 'w') as f:
        flag = False
        t = datetime.now()
        txt = ""
        for item in lst:
            txt = txt + item + '\n'
        f.write(txt)
        if os.path.exists(name):
            logging.info(f"L'écriture du fichier {name} a réussi")

            flag = True

    return flag


def process(lst_origine, lst_exclusion):
    """ Construction de la liste filtrée"""
    return list(set(lst_origine) - set(lst_exclusion))


def list_ecart(lst1, lst2):
    """ Retourne les éléments qui ne figurent que dans 1 seule des 2 listes passées en paramètre"""
    lst = list(set(lst1) ^ set(lst2))
    logging.info(f'Elements figurant dans une seule des 2 listes : {lst}')

    return lst


def add_list(lst1, lst2):
    """fusionne 2 listes passées en parametre"""
    return list((set(lst1) | set(lst2)))


def save_json(lst, nom_fichier='sans_nom'):
    """Sauvegarde au format JSON de la liste passée en paramètre sous le nom nom_fichier"""

    if not os.path.exists(ADRESS_DIR):
        logging.info(f'Création du dossier {ADRESS_DIR}')
        os.makedirs(ADRESS_DIR)
    if not nom_fichier.endswith('json'):
        path = os.path.join(ADRESS_DIR, f'{nom_fichier}.json')
    else:
        path = os.path.join(ADRESS_DIR, nom_fichier)

    path = os.path.join(ADRESS_DIR, FILE_NAME)
    with open(path, 'r') as f:
        all_list = json.load(f)

    all_list[nom_fichier] = lst

    data = {nom_fichier: lst}
    with open(path, "w") as f:
        json.dump(all_list, f, indent=4)
        logging.info(f'Enregistrement du fichier {path}')


def get_lst_from_json(nom_liste='lst_ref'):
    """Renvoie la liste associée à la clef nom_liste du fichier JSON de référence"""

    path = os.path.join(ADRESS_DIR, FILE_NAME)
    if not os.path.exists(path):
        logging.error(f"Le fichier {path} n'existe pas ")
        return
    else:
        with open(path, 'r') as f:
            json_file = json.load(f)
            lst = json_file[nom_liste]
    return list(set(lst))


def get_lst_of_json(path):
    """cette fonction récupére la liste des clefs du fichier json de reference
    """
    path = os.path.join(ADRESS_DIR, FILE_NAME)
    with open(path, 'r') as f:
        all_list = json.load(f)

    return list(all_list.keys())


def add_list_to_json(liste, nom='nouvelle_liste'):
    path = os.path.join(ADRESS_DIR, FILE_NAME)
    with open(path, 'r') as f:
        all_list = json.load(f)

    all_list[nom] = liste
    with open(path, 'w') as f:
        json.dump(all_list, f, indent=4)
        logging.info(f'la liste "{nom}" a été ajouté au fichier {FILE_NAME}')

    return


def remove_list_from_json(nom):
    path = os.path.join(ADRESS_DIR, FILE_NAME)
    with open(path, 'r') as f:
        all_list = json.load(f)

    if not all_list.get(nom):
        logging.info(f'La liste "{nom}" n\'existe pas dans le fichier {FILE_NAME}')
        return False
    else:
        all_list.pop(nom)

    with open(path, 'w') as f:
        json.dump(all_list, f, indent=4)
        logging.info(f'la liste "{nom}" a été retirée au fichier {FILE_NAME}')

    return True


if __name__ == '__main__':
    # test_json = {"toto": [1,2,3], "bibi": [4, 5, 6]}
    # with open("/Users/alainzypinoglou/adress/test_json.json",'w') as f:
    #     json.dump(test_json, f,indent=4)
    #
    # with open("/Users/alainzypinoglou/adress/test_json.json",'r') as f:
    #     all_list = f.read()
    #     print(type(all_list))
    #     print(all_list)
    #     dictio = all_list.split()
    #     print(dictio)

    # import json

    # dict = {"member #002": {"first name": "John", "last name": "Doe", "age": 34},
    #         "member #003": {"first name": "Elijah", "last name": "Baley", "age": 27},
    #         "member #001": {"first name": "Jane", "last name": "Doe", "age": 42}}

    # with open('/Users/alainzypinoglou/adress/test_json.json', 'w') as fp:
    #     json.dump(dict, fp, sort_keys=True, indent=4)
    #
    # with open("/Users/alainzypinoglou/adress/test_json.json", 'r') as f:
    #     all_list = json.load(f)
    #     print(type(all_list))
    #     print(all_list)
    lst1 = ["toto", "bibi", "bibi", "zozor"]
    lst2 = ["tata", "baba", "toto", "bibi", "bibi"]

    # add_list_to_json(lst1, nom="test de liste")
    remove_list_from_json("MaListe")
