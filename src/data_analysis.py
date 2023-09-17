import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from src.utils import load_svg, extract_features
from src.constants import SVG_CHARACTERS_PATH

def analyze_svg(svg_data):
    """
    Analyze the SVG data to identify key features and elements that define a handwriting style.
    """
    # Extract features from the SVG data
    features = extract_features(svg_data)

    # Perform Principal Component Analysis to reduce dimensionality
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(features)

    return pca_result

def analyze_handwriting_styles():
    """
    Analyze the handwriting styles in the SVG characters.
    """
    # Load the SVG characters
    svg_characters = load_svg(SVG_CHARACTERS_PATH)

    # Analyze each SVG character
    analysis_results = {}
    for character, svg_data in svg_characters.items():
        analysis_results[character] = analyze_svg(svg_data)

    return analysis_results

if __name__ == "__main__":
    analysis_results = analyze_handwriting_styles()
    print(analysis_results)