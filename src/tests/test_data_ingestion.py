import unittest
from src.data_ingestion import DataIngestion

class TestDataIngestion(unittest.TestCase):

    def setUp(self):
        self.data_ingestion = DataIngestion()
        self.test_file_path = "resources/test_files/"

    def test_read_svg(self):
        result = self.data_ingestion.read_svg(self.test_file_path + "test.svg")
        self.assertIsNotNone(result, "Failed to read SVG file.")

    def test_parse_svg(self):
        svg_data = self.data_ingestion.read_svg(self.test_file_path + "test.svg")
        result = self.data_ingestion.parse_svg(svg_data)
        self.assertIsNotNone(result, "Failed to parse SVG data.")

    def test_extract_features(self):
        svg_data = self.data_ingestion.read_svg(self.test_file_path + "test.svg")
        parsed_data = self.data_ingestion.parse_svg(svg_data)
        result = self.data_ingestion.extract_features(parsed_data)
        self.assertIsNotNone(result, "Failed to extract features from SVG data.")

if __name__ == '__main__':
    unittest.main()