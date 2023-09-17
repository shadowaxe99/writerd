from tkinter import *


class GUI:
    def __init__(self, svg_files):
        self.window = Tk()
        self.window.title('Handwriting Synthesis Program')
        self.window.geometry('800x600')

        self.svg_files = svg_files

        self.character_label = Label(self.window, text='Select a character:')
        self.character_label.pack()

        self.character_var = StringVar()
        self.character_dropdown = OptionMenu(self.window, self.character_var, *self.svg_files)
        self.character_dropdown.pack()

        self.generate_button = Button(self.window, text='Generate', command=self.generate_style)
        self.generate_button.pack()

        self.window.mainloop()

    def generate_style(self):
        selected_character = self.character_var.get()
        # Logic to generate style for selected character
        pass
