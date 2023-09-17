import unittest
from src import utils

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.svg_file = "resources/test_files/test.svg"
        self.svg_data = utils.read_svg(self.svg_file)

    def test_read_svg(self):
        self.assertIsNotNone(self.svg_data, "Failed to read SVG file")

    def test_extract_features(self):
        features = utils.extract_features(self.svg_data)
        self.assertIsNotNone(features, "Failed to extract features from SVG data")

    def test_generate_style(self):
        style = utils.generate_style(self.svg_data)
        self.assertIsNotNone(style, "Failed to generate style from SVG data")

    def test_save_svg(self):
        output_file = "resources/test_files/output_test.svg"
        utils.save_svg(self.svg_data, output_file)
        self.assertTrue(os.path.exists(output_file), "Failed to save SVG file")

if __name__ == '__main__':
    unittest.main()