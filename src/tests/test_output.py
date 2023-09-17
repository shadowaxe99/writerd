import unittest
from src.output import SVGOutput

class TestOutput(unittest.TestCase):

    def setUp(self):
        self.output = SVGOutput()
        self.test_file_path = "resources/test_files/test.svg"

    def test_generate_svg(self):
        result = self.output.generate_svg("resources/generated_styles/test_style.svg")
        self.assertTrue(result)

    def test_save_svg(self):
        test_style = {
            "stroke": "#000000",
            "stroke-width": "1",
            "fill": "none",
            "d": "M10 10 H 90 V 90 H 10 Z"
        }
        result = self.output.save_svg(test_style, self.test_file_path)
        self.assertTrue(result)

    def test_load_svg(self):
        result = self.output.load_svg(self.test_file_path)
        self.assertIsNotNone(result)

    def test_validate_svg(self):
        test_style = {
            "stroke": "#000000",
            "stroke-width": "1",
            "fill": "none",
            "d": "M10 10 H 90 V 90 H 10 Z"
        }
        result = self.output.validate_svg(test_style)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()