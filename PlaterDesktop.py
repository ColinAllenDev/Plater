import configparser 
import tkinter as tk
from tkinter import ttk
import sv_ttk

class Application:
    def __init__(self, root):
        # Create main window
        self.root = root
        self.root.title("Plater")

        # Create tabs container
        self.notebook = ttk.Notebook(self.root)

        self.tab_editor = ttk.Frame(self.notebook)
        self.tab_options = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_editor, text='Editor')
        self.notebook.add(self.tab_options, text='Options')

        ### EDITOR TAB ###
        # Spacer
        self.label_app = tk.Label(self.tab_editor, text="Plater", font=("Times New Roman", 24))
        self.label_app.grid(row=0, column=1, pady=15)
        
        # Title Field
        self.label_title = tk.Label(self.tab_editor, text="Title")
        self.input_title = tk.Entry(self.tab_editor)        
        self.label_title.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.input_title.grid(row=1, column=1, padx=10, pady=5)
        
        # Tagline Field
        self.label_tagline = tk.Label(self.tab_editor, text="Tagline")
        self.input_tagline = tk.Entry(self.tab_editor)
        self.label_tagline.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        self.input_tagline.grid(row=2, column=1, padx=10, pady=5)
        
        # Mount Field
        self.label_mount = tk.Label(self.tab_editor, text="Mount")
        self.input_mount = tk.Entry(self.tab_editor)
        self.label_mount.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
        self.input_mount.grid(row=3, column=1, padx=10, pady=5)
        
        # Title Field
        self.label_length = tk.Label(self.tab_editor, text="Length")
        self.input_length = tk.Entry(self.tab_editor)
        self.label_length.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
        self.input_length.grid(row=4, column=1, padx=10, pady=5)
        
        # Gain Field
        self.label_gain = tk.Label(self.tab_editor, text="Gain")
        self.input_gain = tk.Entry(self.tab_editor)
        self.label_gain.grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)
        self.input_gain.grid(row=5, column=1, padx=10, pady=5)
        
        # Power Field
        self.label_power = tk.Label(self.tab_editor, text="Power")
        self.input_power = tk.Entry(self.tab_editor)
        self.label_power.grid(row=6, column=0, padx=10, pady=5, sticky=tk.E)
        self.input_power.grid(row=6, column=1, padx=10, pady=5)
        
        # Metadata Field
        self.label_metadata = tk.Label(self.tab_editor, text="Metadata")
        self.label_metadata.grid(row=0, rowspan=2, column=2, padx=60, pady=5, sticky=tk.E)
        self.input_metadata_1 = tk.Entry(self.tab_editor)
        self.input_metadata_1.grid(row=1, column=2, padx=10, pady=5)
        self.input_metadata_2 = tk.Entry(self.tab_editor)
        self.input_metadata_2.grid(row=2, column=2, padx=10, pady=5)
        self.input_metadata_3 = tk.Entry(self.tab_editor)
        self.input_metadata_3.grid(row=3, column=2, padx=10, pady=5)

        # Submit Button
        self.input_submit = tk.Button(self.tab_editor, text='Save', command=self.generate_svg)
        self.input_submit.grid(row=7, column=2, columnspan=2, pady=10)

        ### OPTIONS TAB ###
        # Initialize options input fields
        self.label_font_family = tk.Label(self.tab_options, text="Font")
        self.input_font_family = tk.Entry(self.tab_options)
        self.label_font_family.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.input_font_family.grid(row=1, column=1, padx=10)
        self.input_font_family.insert(0, 'Bahnschrift')

        self.label_path = tk.Label(self.tab_options, text="Path")
        self.input_path = tk.Entry(self.tab_options)
        self.label_path.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        self.input_path.grid(row=2, column=1, padx=10)
        self.input_path.insert(0, '')

        self.notebook.pack(expand=True, fill='both')


        # Display success text
        self.message_success = tk.Label(self.tab_editor,   text=f'Successfully saved {self.input_title.get()}')
        self.message_success.grid(row=7, column=1, pady=5, sticky=tk.E)



if __name__ == "PlaterDesktop":
    # Read configuration file
    config = configparser.ConfigParser().read('config.ini')['DEFAULT']
    
    root = tk.Tk()
    app = Application(root)
    sv_ttk.set_theme("dark")
    root.mainloop()
