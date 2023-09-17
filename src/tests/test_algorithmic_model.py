import unittest
from src.models.algorithmic_model import AlgorithmicModel

class TestAlgorithmicModel(unittest.TestCase):

    def setUp(self):
        self.model = AlgorithmicModel()

    def test_generate_style(self):
        input_svg = "resources/test_files/test.svg"
        output_svg = "resources/generated_styles/test_style.svg"
        self.model.generate_style(input_svg, output_svg)
        self.assertTrue(os.path.exists(output_svg))

    def test_generate_style_with_invalid_input(self):
        with self.assertRaises(FileNotFoundError):
            self.model.generate_style("invalid.svg", "output.svg")

    def test_generate_style_with_invalid_output(self):
        with self.assertRaises(FileNotFoundError):
            self.model.generate_style("resources/test_files/test.svg", "invalid/output.svg")

if __name__ == '__main__':
    unittest.main()