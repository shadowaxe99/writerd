
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from src.utils import load_data, preprocess_data
from src.constants import SVG_CHARACTERS_PATH

class HandwritingModel:
    def __init__(self):
        self.model = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500)

    def train_model(self):
        # Load and preprocess data
        data, labels = load_data(SVG_CHARACTERS_PATH)
        data = preprocess_data(data)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

        # Train the model
        self.model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy}")

    def generate_handwriting(self, input_data):
        # Preprocess input data
        input_data = preprocess_data(input_data)

        # Generate handwriting style
        output = self.model.predict(input_data)
        return output
