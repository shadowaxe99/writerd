```python
import unittest
from src.style_generation import StyleGenerator
from src.data_ingestion import DataIngestor
from src.data_analysis import DataAnalyzer
from src.constants import SVG_CHARACTERS_PATH

class TestStyleGeneration(unittest.TestCase):

    def setUp(self):
        self.data_ingestor = DataIngestor(SVG_CHARACTERS_PATH)
        self.data_analyzer = DataAnalyzer(self.data_ingestor.data)
        self.style_generator = StyleGenerator(self.data_analyzer.features)

    def test_generate_style(self):
        new_style = self.style_generator.generate_style()
        self.assertIsNotNone(new_style)

    def test_save_style(self):
        new_style = self.style_generator.generate_style()
        save_path = self.style_generator.save_style(new_style)
        self.assertTrue(os.path.exists(save_path))

if __name__ == '__main__':
    unittest.main()
```