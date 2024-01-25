import tomllib
import drawsvg as draw
import subprocess

class Plater:
    def __init__(self):
        with open('config.toml', 'rb') as f:
            self.config = tomllib.load(f)

        self.width = self.config['Width']
        self.height = self.config['Height']
        self.title_position = {'x': self.width / 2, 'y': self.config['FontSpacingMajor']}
        self.tagline_position = {'x': self.width / 2, 'y': (self.title_position['y'] * 2) + self.config['FontSpacingMinor']}
        self.length_position = {'x': self.config['FontSpacingMinor'], 'y': self.height - self.config['FontSpacingMajor']}
        self.mount_position = {'x': self.config['FontSpacingMinor'], 'y': self.length_position['y'] - self.config['FontSpacingMajor']}
        self.gain_position = {'x': self.width - self.config['FontSpacingMinor'], 'y': self.mount_position['y']}
        self.power_position = {'x': self.width - self.config['FontSpacingMinor'] , 'y': self.length_position['y']}

    def draw(self, data):
        self.plate = draw.Drawing(self.width, self.height, origin=(0, 0),
                                  context=None, animation_config=None, id_prefix='d')
        self.plate.set_render_size(self.width, self.height)

        # Title
        self.plate.append(draw.Text(data['title'], 
                               font_size=self.config['FontSizeTitle'], 
                               font_family=data['font_family'], 
                               center=True, 
                               fill='white', 
                               x=self.title_position['x'], 
                               y=self.title_position['y']))

        
        # Tagline
        self.plate.append(draw.Text(data['tagline'],
                               font_size=self.config['FontSizeTagline'],
                               font_family=data['font_family'],
                               fill='white',
                               center=True, 
                               x=self.tagline_position['x'],
                               y=self.tagline_position['y']))

        # Metadata
        self.plate.append(draw.Text(data['metadata'],
                               font_size=self.config['FontSizeMetadata'],
                               font_family=data['font_family'],
                               fill='white',
                               center=True,
                               text_anchor='middle',
                               x=self.width / 2,
                               y=self.height / 2))

        # Mount
        self.plate.append(draw.Text(f'Mount: {data["mount"]}',
                               font_size=self.config['FontSizeInfo'],
                               font_family=data['font_family'],
                               fill='white',
                               center=True,
                               text_anchor='start',
                               x=self.mount_position['x'],
                               y=self.mount_position['y']))

        # Length
        self.plate.append(draw.Text(f'Length: {data["length"]}',
                               font_size=self.config['FontSizeInfo'],
                               font_family=data['font_family'],
                               fill='white',
                               center=True,
                               text_anchor='start',
                               x=self.length_position['x'],
                               y=self.length_position['y']))

        # Gain
        self.plate.append(draw.Text(f'Gain: {data["gain"]}',
                               font_size=self.config['FontSizeInfo'],
                               font_family=data['font_family'],
                               fill='white',
                               center=True,
                               text_anchor='end',
                               x=self.gain_position['x'],
                               y=self.gain_position['y']))

        # Power
        self.plate.append(draw.Text(f'Power: {data["power"]}',
                               font_size=self.config['FontSizeInfo'],
                               font_family=data['font_family'],
                               fill='white',
                               center=True,
                               text_anchor='end',
                               x=self.power_position['x'],
                               y=self.power_position['y']))
        
    def generate_svg(self, data):
        try:
            final_path = ''
            if (data["input_path"] == ''):
                final_path = f'{data["title"]}.svg';
            else:
                final_path = f'{data["input_path"].rstrip("/")}/{data["title"].replace("/", "-")}.svg'
            
            self.plate.save_svg(final_path)
            
            subprocess.call(f'inkscape --file={final_path} --export-plain-svg={final_path} --export-text-to-path', shell = True)

            
            return final_path
        except Exception as exc:
            raise RuntimeError("Something went wrong!") from exc
