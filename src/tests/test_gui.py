```python
import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import sys

# Import the GUI
from src.gui import HandwritingSynthesisGUI

app = QApplication(sys.argv)

class TestGUI(unittest.TestCase):
    def setUp(self):
        self.form = HandwritingSynthesisGUI()

    def test_defaults(self):
        """
        Test the GUI in its default state
        """
        self.assertEqual(self.form.ui.inputText.text(), "")
        self.assertEqual(self.form.ui.outputSVG.text(), "")

    def test_input_text(self):
        """
        Test the input text field
        """
        self.form.ui.inputText.setText("Test")
        self.assertEqual(self.form.ui.inputText.text(), "Test")

    def test_output_svg(self):
        """
        Test the output SVG field
        """
        self.form.ui.outputSVG.setText("Test.svg")
        self.assertEqual(self.form.ui.outputSVG.text(), "Test.svg")

    def test_generate_button(self):
        """
        Test the generate button
        """
        QTest.mouseClick(self.form.ui.generateButton, Qt.LeftButton)
        self.assertEqual(self.form.ui.outputSVG.text(), "Generated.svg")

if __name__ == "__main__":
    unittest.main()
```