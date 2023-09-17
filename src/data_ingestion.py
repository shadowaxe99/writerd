import os


class DataIngestion:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def read_svg_files(self):
        svg_files = []
        for file_name in os.listdir(self.data_dir):
            if file_name.endswith('.svg'):
                file_path = os.path.join(self.data_dir, file_name)
                svg_files.append(file_path)
        return svg_files
