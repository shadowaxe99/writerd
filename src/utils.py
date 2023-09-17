import os
import numpy as np
from xml.dom import minidom
from src.constants import SVG_CHARACTERS_PATH


def load_data():
    """
    Load SVG data from the SVG_CHARACTERS_PATH directory.
    """
    data = []
    labels = []

    svg_files = os.listdir(SVG_CHARACTERS_PATH)

    for file in svg_files:
        file_path = os.path.join(SVG_CHARACTERS_PATH, file)
        svg_doc = minidom.parse(file_path)
        paths = svg_doc.getElementsByTagName('path')
        path_data = [path.getAttribute('d') for path in paths]
        data.append(path_data)
        labels.append(file)

    return np.array(data), np.array(labels)


def preprocess_data(data):
    """
    Preprocess the SVG data.
    """
    # Perform preprocessing steps
    preprocessed_data = data

    return preprocessed_data


def get_svg_paths(file_path):
    """
    Extract all the path elements from an SVG file.
    """
    svg_doc = minidom.parse(file_path)
    paths = svg_doc.getElementsByTagName('path')
    return [path.getAttribute('d') for path in paths]


def load_svg(file_path):
    """
    Load an SVG file and return the document object.
    """
    return minidom.parse(file_path)
