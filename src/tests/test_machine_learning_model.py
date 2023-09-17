import unittest
from src.models.machine_learning_model import MachineLearningModel
from src.utils import load_svg, preprocess_data
from src.constants import SVG_CHARACTERS_PATH

class TestMachineLearningModel(unittest.TestCase):

    def setUp(self):
        self.model = MachineLearningModel()
        self.svg_data = load_svg(SVG_CHARACTERS_PATH)

    def test_model_creation(self):
        self.assertIsInstance(self.model, MachineLearningModel)

    def test_preprocessing(self):
        preprocessed_data = preprocess_data(self.svg_data)
        self.assertIsNotNone(preprocessed_data)

    def test_model_training(self):
        preprocessed_data = preprocess_data(self.svg_data)
        self.model.train(preprocessed_data)
        self.assertTrue(self.model.is_trained)

    def test_model_prediction(self):
        preprocessed_data = preprocess_data(self.svg_data)
        self.model.train(preprocessed_data)
        prediction = self.model.predict(preprocessed_data[0])
        self.assertIsNotNone(prediction)

if __name__ == '__main__':
    unittest.main()