```python
import os
from xml.dom import minidom
from src.constants import GENERATED_STYLES_PATH

def create_svg_file(style, filename):
    """
    Function to create a new SVG file based on the generated style.
    """
    doc = minidom.Document()

    svg = doc.createElement('svg')
    doc.appendChild(svg)

    path = doc.createElement('path')
    path.setAttribute('d', style)
    svg.appendChild(path)

    with open(os.path.join(GENERATED_STYLES_PATH, filename), 'w') as f:
        f.write(doc.toprettyxml(indent="  "))

def output_generated_styles(styles):
    """
    Function to output the generated styles as SVG files.
    """
    for i, style in enumerate(styles):
        create_svg_file(style, f"style_{i}.svg")
```