```python
import sys
from PyQt5.QtWidgets import QApplication

from src.gui import HandwritingSynthesisGUI
from src.data_ingestion import DataIngestion
from src.data_analysis import DataAnalysis
from src.style_generation import StyleGeneration
from src.output import Output

def main():
    app = QApplication(sys.argv)

    data_ingestion = DataIngestion()
    data_analysis = DataAnalysis()
    style_generation = StyleGeneration()
    output = Output()

    svg_data = data_ingestion.read_svg_files("resources/svg_characters/")
    analyzed_data = data_analysis.analyze_data(svg_data)
    new_styles = style_generation.generate_styles(analyzed_data)
    output.generate_svg_files(new_styles, "resources/generated_styles/")

    gui = HandwritingSynthesisGUI()
    gui.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
```