import configparser 
import drawsvg as draw

class Plater:
    def __init__(self, config):
        self.width = config['WidthIn'] * config['dpi']
        self.height = config['HeightIn'] * config['dpi']
        self.title_position = {'x': self.width / 2, 'y': config['FontSpacingMajor']}
        self.tagline_position = {'x': self.width / 2, 'y': (self.title_position * 2) + config['FontSpacingMinor']}
        self.length_position = {'x': config['FontSpacingMinor'], 'y': self.height - config['FontSpacingMajor']}
        self.mount_position = {'x': config['FontSpacingMinor'], 'y': self.length_position['y'] - config['FontSpacingMinor']}
        self.gain_position = {'x': self.width - config['FontSpacingMinor'], 'y': self.mount_position['y']}
        self.power_position = {'x': self.width - config['FontSpacingMinor'] , 'y': self.length_position['y']}

    def generate_svg(self):
        plate = draw.Drawing(self.width, self.height)
        plate.set_render_size(self.width, self.height)

        # Placeholder frame
        plate.append(draw.Rectangle(0, 0, self.width, self.height, fill_opacity=0, stroke='white'))

        # Title
        plate.append(draw.Text(self.input_title.get(), 
                               font_size=config['FontSizeTitle'], 
                               font_family=self.input_font_family.get(), 
                               center=True, 
                               fill='white', 
                               x=self.title_position['x'], 
                               y=self.title_position['y']))

        # Tagline
        plate.append(draw.Text(self.input_tagline.get(),
                               font_size=config['FontSizeTagline'],
                               font_family=self.input_font_family.get(),
                               fill='white',
                               center=True, 
                               x=self.tagline_position['x'],
                               y=self.tagline_position['y']))

        # Metadata
        plate.append(draw.Text([self.input_metadata_1.get(),
                                self.input_metadata_2.get(),
                                self.input_metadata_3.get()],
                               font_size=config['FontSizeMetadata'],
                               font_family=self.input_font_family.get(),
                               fill='white',
                               center=True,
                               text_anchor='middle',
                               x=self.width / 2,
                               y=self.width / 2))

        # Mount
        plate.append(draw.Text(f'Mount: {self.input_mount.get()}',
                               font_size=config['FontSizeInfo'],
                               font_family=self.input_font_family.get(),
                               fill='white',
                               center=True,
                               text_anchor='start',
                               x=self.mount_position['x'],
                               y=self.mount_position['y']))

        # Length
        plate.append(draw.Text(f'Length: {self.input_length.get()}',
                               font_size=config['FontSizeInfo'],
                               font_family=self.input_font_family.get(),
                               fill='white',
                               center=True,
                               text_anchor='start',
                               x=self.length_position['x'],
                               y=self.length_position['y']))

        # Gain
        plate.append(draw.Text(f'Gain: {self.input_gain.get()}',
                               font_size=config['FontSizeInfo'],
                               font_family=self.input_font_family.get(),
                               fill='white',
                               center=True,
                               text_anchor='end',
                               x=self.gain_position['x'],
                               y=self.gain_position['y']))

        # Power
        plate.append(draw.Text(f'Power: {self.input_power.get()}',
                               font_size=config['FontSizeInfo'],
                               font_family=self.input_font_family.get(),
                               fill='white',
                               center=True,
                               text_anchor='end',
                               x=self.power_position['x'],
                               y=self.power_position['y']))
        # Save svg
        final_path = ''
        if (self.input_path.get() == ''):
            final_path = f'{self.input_title.get()}.svg';
        else:
            final_path = f'{self.input_path.get().rstrip("/")}/{self.input_title.get().replace("/", "-")}.svg'
        plate.save_svg(final_path)

        # Display success text
        self.message_success = tk.Label(self.tab_editor,   text=f'Successfully saved {self.input_title.get()}')
        self.message_success.grid(row=7, column=1, pady=5, sticky=tk.E)


# Main
config = configparser.ConfigParser().read('config.ini')['DEFAULT']

