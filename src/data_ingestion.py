```python
import os
from xml.dom import minidom
from src.constants import SVG_CHARACTERS_PATH
from src.utils import get_svg_paths

def parse_svg(file_path):
    """
    Parse an SVG file and return the document object.
    """
    return minidom.parse(file_path)

def extract_paths(svg_doc):
    """
    Extract all the path elements from an SVG document.
    """
    paths = svg_doc.getElementsByTagName('path')
    return [path.getAttribute('d') for path in paths]

def read_svg_files():
    """
    Read all SVG files in the resources directory and return a dictionary
    mapping file names to their path data.
    """
    svg_files = os.listdir(SVG_CHARACTERS_PATH)
    svg_data = {}

    for file in svg_files:
        file_path = os.path.join(SVG_CHARACTERS_PATH, file)
        svg_doc = parse_svg(file_path)
        svg_data[file] = extract_paths(svg_doc)

    return svg_data

def ingest_data():
    """
    Ingest data from SVG files and return a dictionary mapping file names
    to their path data.
    """
    svg_data = read_svg_files()
    return svg_data
```