# -*- coding: utf-8 -*-
import logging
import json
import os
import sys
from glob import glob
from pathlib import Path
from datetime import datetime
from pprint import pprint

if sys.platform == 'win32':
    ADRESS_DIR = f'D{os.path.join(Path.home(), "adress")[1:]}'
else:
    ADRESS_DIR = os.path.join(Path.home(), "adress")


FILE_NAME = 'lst_ref.json'

logging.basicConfig(level=logging.DEBUG)


def txt_to_lst(text=""):

        lst = text.split(';')
        lst1 = [item.split('<')[1][:-1] for item in lst if '<' in item and '--'in item and 'mar' in item]
        lst2 = [item.split('<')[1][:-1] for item in lst if '<' in item and not '--' in item]
        lst3 = list(set(lst2))
        if lst2:
            logging.error("la liste contient des listes d'adresses")

        pprint(lst2)
        pprint(len(lst3))
        pprint(lst1)

        return lst3


def write_to_disk(path, lst):
    p = os.path.dirname(path)
    b = os.path.basename(path)
    t = os.path.splitext(b)
    name = os.path.join(os.path.dirname(path), f'{t[0]}.txt')

    if not os.path.exists(ADRESS_DIR):
        os.makedirs(ADRESS_DIR)

    with open(name, 'w') as f:
        flag = False
        t = datetime.now()
        # horodatage = str(t.date())+"-"+str(t.time())[:-7]
        # txt = horodatage +";" +"\n"
        txt = ""
        # print(lst)
        for item in lst:
            txt = txt + item + '\n'
        f.write(txt)
        if os.path.exists(name):
            logging.info(f"L'écriture du fichier {name} a réussi")

            flag = True

    return flag


def process(lst_origine, lst_exclusion):
    """ Construction de la liste filtrée"""
    lst = list(set(lst_origine) - set(lst_exclusion))
    # lst = [item for item in lst_origine if item not in lst_exclusion]
    return lst


# def get_file_to_list(path):
#     with open(path, 'r') as f:
#         txt = f.read().lower()
#         lst = txt.split()
#         return lst


def list_ecart(lst1, lst2):
    """ Retourne les éléments qui ne figurent que dans 1 seule des 2 listes passées en paramètre"""
    # a = set(lst1)
    # b = set(lst2)
    # c = list(a ^ b)
    lst = list(set(lst1) ^ set(lst2))
    logging.info(f'Elements figurant dans une seule des 2 listes : {lst}')

    return lst


def save_json(lst, nom_fichier='sans_nom'):
    """Sauvegarde au format JSON de la liste passée en paramètre sous le nom nom_fichier"""

    if not os.path.exists(ADRESS_DIR):
        logging.info(f'Création du dossier {ADRESS_DIR}')
        os.makedirs(ADRESS_DIR)
    if not nom_fichier.endswith('json'):
        path = os.path.join(ADRESS_DIR, f'{nom_fichier}.json')
    else:
        path = os.path.join(ADRESS_DIR, nom_fichier)


    # path = os.path.join(ADRESS_DIR, FILE_NAME)

    data = {nom_fichier: lst}
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        logging.info(f'Enregistrement du fichier {path}')


def get_lst_from_json(path, nom_liste='lst_ref'):
    """Récupère le liste de clef nom_liste dans le fichier Json indiqué dans le paramètre path"""


    if not os.path.exists(path):
        logging.error(f"Le fichier {path} n'existe pas ")
        return
    else:
        with open(path, 'r') as f:
            json_file = json.load(f)
            lst = json_file[nom_liste]
    return lst


def get_lst_of_json(path):
    """récupère la liste des fichiers json
    *** cette fonction doit etre modifiée pour ne récupérer que
     la liste des clefs du fichier json de reference ***
    """

    lst_json = glob(f"{path}/*.json")
    return lst_json


if __name__ == '__main__':


    ADRESS_DIR = '/Users/alainzypinoglou/adress'
    lst1 = [1, 2, 3, 4, 5]
    lst2 = [1, 2, 6, 7, 8]
    save_json(lst1, "toto")

    # path = '/Users/alainzypinoglou/adress/'
    # lst = get_lst_of_json(path=path)
    # print(lst)









