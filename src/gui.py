import tkinter as tk
from tkinter import filedialog, messagebox
from src import data_ingestion, data_analysis, style_generation, output, constants

class HandwritingSynthesisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Handwriting Synthesis')
        self.create_widgets()

    def create_widgets(self):
        self.upload_button = tk.Button(self.root, text='Upload SVG', command=self.upload_svg)
        self.upload_button.pack()

        self.generate_button = tk.Button(self.root, text='Generate Handwriting', command=self.generate_handwriting)
        self.generate_button.pack()

        self.save_button = tk.Button(self.root, text='Save Generated Style', command=self.save_generated_style)
        self.save_button.pack()

    def upload_svg(self):
        self.filepath = filedialog.askopenfilename(filetypes=[('SVG files', '*.svg')])
        if self.filepath:
            self.svg_data = data_ingestion.read_svg(self.filepath)
            self.analyzed_data = data_analysis.analyze_svg(self.svg_data)

    def generate_handwriting(self):
        if self.analyzed_data:
            self.generated_style = style_generation.generate_style(self.analyzed_data)
        else:
            messagebox.showerror('Error', 'No SVG file uploaded.')

    def save_generated_style(self):
        if self.generated_style:
            save_path = filedialog.asksaveasfilename(defaultextension=".svg")
            output.save_svg(self.generated_style, save_path)
        else:
            messagebox.showerror('Error', 'No generated style to save.')

if __name__ == "__main__":
    root = tk.Tk()
    app = HandwritingSynthesisGUI(root)
    root.mainloop()