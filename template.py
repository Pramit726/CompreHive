import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name= "compgenerator"

list_of_files=[
    "notebooks\comp_generator.ipynb",
    "src/__init__.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/compgenerator.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    ".streamlit\config.toml"
    ".env",
    ".gitignore",
    "response.json",
    "README.md",
    "app.py",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")
