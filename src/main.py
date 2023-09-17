from tkinter import *
from data_ingestion import DataIngestion
from data_analysis import DataAnalysis
from style_generation import StyleGeneration
from output_generation import OutputGeneration
from gui import GUI


def main():
    data_dir = 'data'

    # Data Ingestion
    data_ingestion = DataIngestion(data_dir)
    svg_files = data_ingestion.read_svg_files()

    # Data Analysis
    data_analysis = DataAnalysis()
    features = data_analysis.identify_features(svg_files[0])

    # Style Generation
    style_generation = StyleGeneration()
    new_style = style_generation.generate_style(features)

    # Output Generation
    output_generation = OutputGeneration()
    output_generation.generate_svg_files()

    # GUI
    gui = GUI(svg_files)


if __name__ == '__main__':
    main()
