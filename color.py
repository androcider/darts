import pyray
import os
from PIL import Image
class Color:
    """A color.

    The responsibility of Color is to hold and provide information about itself. Color has a few 
    convenience methods for comparing them and converting to a tuple.

    Attributes:
        _red (int): The red value.
        _green (int): The green value.
        _blue (int): The blue value.
        _alpha (int): The alpha or opacity.
    """
    
    def __init__(self, red, green, blue, alpha = 255):
        """Constructs a new Color using the specified red, green, blue and alpha values. The alpha 
        value is the color's opacity.
        
        Args:
            red (int): A red value.
            green (int): A green value.
            blue (int): A blue value.
            alpha (int): An alpha or opacity.
        """
        print('here')
        self._red = red
        self._green = green
        self._blue = blue 
        self._alpha = alpha

    def to_tuple(self):
        """Gets the color as a tuple of four values (red, green, blue, alpha).

        Returns:
            Tuple(int, int, int, int): The color as a tuple.
        """
        return (self._red, self._green, self._blue, self._alpha)   
    def get_color(self,x_pixel,y_pixel):
        color = pyray.get_pixel_color(x_pixel,y_pixel)
        return color

    def get_r_g_b(self, x,y):
        background=  os.path.dirname(os.path.abspath(__file__)) + "\\background.PNG"
        image_original = Image.open(background)

        pixels_original = image_original.load()
        r,g,b,a = pixels_original[x,y]
        print (f'{r},{g},{b},{a}')
        return (r,g,b)