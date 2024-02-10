#!/usr/bin/env python3

import os  # Importe le module os pour les opérations liées au système d'exploitation
import shutil  # Importe le module shutil pour les opérations de haut niveau sur les fichiers
import datetime  # Importe le module datetime pour travailler avec des objets de date et d'heure
import time  # Importe le module time pour les fonctions liées au temps


source_dir = "/home/student/Schreibtisch/"
destination_dir = "/home/student/Dokumente/backup"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

copy_folder_to_directory(source_dir, destination_dir)
