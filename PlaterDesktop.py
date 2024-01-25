from plater import Plater
import tkinter as tk
from tkinter import ttk
import sv_ttk

class Application:
    def __init__(self, root):
        # Create main window
        self.root = root
        self.root.title("Plater")

        # Create tabs container
        notebook = ttk.Notebook(root)

        self.tab_editor = ttk.Frame(notebook)
        self.tab_options = ttk.Frame(notebook)

        notebook.add(self.tab_editor, text='Editor')
        notebook.add(self.tab_options, text='Options')

        self.initialize_editor()
        self.initialize_options()

        # Pack notebook with tab data
        notebook.pack(expand=True, fill='both')

        # Submit Buttons
        btn_save_svg = tk.Button(self.tab_editor, text='Export SVG', command=lambda: self.generate_image('svg'))
        btn_save_svg.grid(row=7, column=2, columnspan=2, pady=10)

    def initialize_editor(self):
        # Spacer
        label_app = tk.Label(self.tab_editor, text="Plater", font=("Times New Roman", 24))
        label_app.grid(row=0, column=1, pady=15)
        
        # Title Field
        label_title = tk.Label(self.tab_editor, text="Title")
        label_title.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

        self.input_title = tk.Entry(self.tab_editor)        
        self.input_title.grid(row=1, column=1, padx=10, pady=5)
        
        # Tagline Field
        label_tagline = tk.Label(self.tab_editor, text="Tagline")
        label_tagline.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)

        self.input_tagline = tk.Entry(self.tab_editor)
        self.input_tagline.grid(row=2, column=1, padx=10, pady=5)
        
        # Mount Field
        label_mount = tk.Label(self.tab_editor, text="Mount")
        label_mount.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)

        self.input_mount = tk.Entry(self.tab_editor)
        self.input_mount.grid(row=3, column=1, padx=10, pady=5)
        
        # Length Field
        label_length = tk.Label(self.tab_editor, text="Length")
        label_length.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)

        self.input_length = tk.Entry(self.tab_editor)
        self.input_length.grid(row=4, column=1, padx=10, pady=5)
        
        # Gain Field
        label_gain = tk.Label(self.tab_editor, text="Gain")
        label_gain.grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)

        self.input_gain = tk.Entry(self.tab_editor)
        self.input_gain.grid(row=5, column=1, padx=10, pady=5)
        
        # Power Field
        label_power = tk.Label(self.tab_editor, text="Power")
        label_power.grid(row=6, column=0, padx=10, pady=5, sticky=tk.E)

        self.input_power = tk.Entry(self.tab_editor)
        self.input_power.grid(row=6, column=1, padx=10, pady=5)
        
        # Metadata Field
        label_metadata = tk.Label(self.tab_editor, text="Metadata")
        label_metadata.grid(row=0, rowspan=2, column=2, padx=60, pady=5, sticky=tk.E)
        self.input_metadata_1 = tk.Entry(self.tab_editor)
        self.input_metadata_1.grid(row=1, column=2, padx=10, pady=5)
        self.input_metadata_2 = tk.Entry(self.tab_editor)
        self.input_metadata_2.grid(row=2, column=2, padx=10, pady=5)
        self.input_metadata_3 = tk.Entry(self.tab_editor)
        self.input_metadata_3.grid(row=3, column=2, padx=10, pady=5)

    def initialize_options(self):
        # Initialize options input fields
        label_font_family = tk.Label(self.tab_options, text="Font")
        label_font_family.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

        self.input_font_family = tk.Entry(self.tab_options)
        self.input_font_family.grid(row=1, column=1, padx=10)
        self.input_font_family.insert(0, 'Bahnschrift')

        label_path = tk.Label(self.tab_options, text="Path")
        label_path.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        
        self.input_path = tk.Entry(self.tab_options)
        self.input_path.grid(row=2, column=1, padx=10)
        self.input_path.insert(0, '')

    def generate_image(self, type):
        # Get Data
        input_data = {}
        input_data['font_family'] = self.input_font_family.get()
        input_data['input_path'] = self.input_path.get()
        input_data['title'] = self.input_title.get()
        input_data['tagline'] = self.input_tagline.get()
        input_data['mount'] = self.input_mount.get()
        input_data['length'] = self.input_length.get()
        input_data['gain'] = self.input_gain.get()
        input_data['power'] = self.input_power.get()
        input_data['metadata'] = [self.input_metadata_1.get(),
                                  self.input_metadata_2.get(),
                                  self.input_metadata_3.get()]

        # Initialize plater API
        plater = Plater()
        plater.draw(input_data)
        plate_path = plater.generate_svg(input_data)

        # Display success text
        message_success = tk.Label(self.tab_editor, text=f'Successfully saved {plate_path}')
        message_success.grid(row=7, column=1, pady=5, sticky=tk.E)



# Initialize desktop application
root = tk.Tk()
app = Application(root)
sv_ttk.set_theme("dark")
root.mainloop()
