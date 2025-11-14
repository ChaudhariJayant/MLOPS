import os
from box.exceptions import BoxValueError
import yaml
import logging
import json
import joblib
from ensure import ensure_annotations # pyright: ignore[reportMissingImports]
from box import ConfigBox
from pathlib import Path
from typing import Any

logger = logging.getLogger("mlProjectLogger")

@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """Reads a yaml file and returns
    Args:
        path_to_yaml (Path): Path like input
    Raises:
        e: Raises an exception if yaml file is not found
    Returns:
        ConfigBox: ConfigBox type object
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise BoxValueError("yaml file is empty")
    except Exception as e:
        logger.exception(e)
        raise e 

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories
    Args:
        path_to_directories (list): List of path of directories
        verbose (bool, optional): Defaults to True. Whether to log info or not
    """
    for path_to_directory in path_to_directories:
        os.makedirs(path_to_directory, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path_to_directory}")

@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """Saves a dictionary to a json file
    Args:
        path (Path): Path to the json file
        data (dict): Data to be saved
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"Json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a json file to a ConfigBox object
    Args:
        path (Path): Path to the json file
    Returns:
        ConfigBox: ConfigBox object
    """
    with open(path, "r") as f:
        content = json.load(f)
    logger.info(f"Json file loaded from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(file_path: Path, data: Any): 
    """Saves data in binary format using joblib
    Args:
        file_path (Path): Path to the binary file
        data (Any): Data to be saved
    """
    with open(file_path, "wb") as file_obj:
        joblib.dump(data, file_obj)
    logger.info(f"Binary file saved at: {file_path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """Get size in KB
    Args:
        path (Path): Path to the file
    Returns:
        str: Size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"