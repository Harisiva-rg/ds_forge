import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

projectName = "Empty_Project"

file_list  = [
    ".github/workflows/.gitkeep",
    f"src/{projectName}/__init__.py",
    f"src/{projectName}/modules/__init__.py",
    f"src/{projectName}/utilities/__init__.py",
    f"src/{projectName}/pipeline/__init__.py",
    f"src/{projectName}/constants/__init__.py",
    "models/.gitkeep",
    "data/raw/.gitkeep",
    "data/intermediate/.gitkeep",
    "data/processed/.gitkeep",
    "reports/.gitkeep",
    "research/experiments.ipynb",
    "tests/.gitkeep",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "README.md"
]


for filepath in file_list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Created directory: {filedir}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")