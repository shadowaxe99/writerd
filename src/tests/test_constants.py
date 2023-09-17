import unittest
from src import constants

class TestConstants(unittest.TestCase):

    def test_constants(self):
        self.assertEqual(constants.SVG_CHARACTERS_PATH, "resources/svg_characters/")
        self.assertEqual(constants.GENERATED_STYLES_PATH, "resources/generated_styles/")
        self.assertEqual(constants.TEST_FILES_PATH, "resources/test_files/")
        self.assertIsNotNone(constants.MACHINE_LEARNING_MODEL_PATH)
        self.assertIsNotNone(constants.ALGORITHMIC_MODEL_PATH)

if __name__ == '__main__':
    unittest.main()