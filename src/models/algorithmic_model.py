```python
import numpy as np
from src.utils import svg_to_points, points_to_svg

class AlgorithmicModel:
    def __init__(self):
        self.styles = []

    def train(self, svg_files):
        for svg_file in svg_files:
            points = svg_to_points(svg_file)
            self.styles.append(self.extract_style(points))

    def extract_style(self, points):
        # This is a placeholder for the actual style extraction algorithm
        # The actual implementation would depend on the specific algorithm used
        return np.mean(points, axis=0)

    def generate(self, style_index, character):
        # This is a placeholder for the actual generation algorithm
        # The actual implementation would depend on the specific algorithm used
        style = self.styles[style_index]
        points = svg_to_points(character)
        new_points = points + style
        return points_to_svg(new_points)
```