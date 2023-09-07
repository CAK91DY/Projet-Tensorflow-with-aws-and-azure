# Importation des modules nécessaires
import os
from pathlib import Path
import logging

# Configuration de la journalisation
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Définition du nom du projet
project_name = "cnnClassifier"

# Liste des fichiers et répertoires nécessaires pour le projet
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
    
]

# Parcours de la liste des fichiers et répertoires
for filepath in list_of_files:
    # Convertir le chemin en objet Path
    filepath = Path(filepath)
    # Extraire le répertoire et le nom de fichier du chemin
    filedir, filename = os.path.split(filepath)

    # Vérification et création des répertoires
    if filedir != "":
        # Création du répertoire avec exist_ok=True pour éviter les erreurs si le répertoire existe déjà
        os.makedirs(filedir, exist_ok=True)
        # Journalisation de la création du répertoire
        logging.info(f"Creation du répertoire; {filedir} pour le fichier: {filename}")

    # Vérification et création des fichiers
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Si le fichier n'existe pas ou est vide, créez un fichier vide
        with open(filepath, "w") as f:
            pass
        # Journalisation de la création du fichier vide
        logging.info(f"Création du fichier vide: {filepath}")
    else:
        # Journalisation indiquant que le fichier existe déjà
        logging.info(f"{filename} le fichier existe déjà")
