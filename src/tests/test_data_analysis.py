import pytest
from src.data_analysis import DataAnalysis

def test_data_analysis():
    data_analysis = DataAnalysis()

    # Test if the SVG files are correctly loaded
    assert data_analysis.load_svg_files('resources/svg_characters/') is not None, "SVG files loading failed"

    # Test if the key features are correctly identified
    assert data_analysis.identify_key_features() is not None, "Key features identification failed"

    # Test if the elements in the SVGs are correctly identified
    assert data_analysis.identify_svg_elements() is not None, "SVG elements identification failed"

    # Test if the handwriting style is correctly defined
    assert data_analysis.define_handwriting_style() is not None, "Handwriting style definition failed"

if __name__ == "__main__":
    pytest.main()