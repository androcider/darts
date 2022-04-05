import pyray
from sympy import O
from point import Point



class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self, cell_size = 1):
        """Constructs a new KeyboardService using the specified cell size.
        
        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._cell_size = cell_size

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1
        
        if pyray.is_key_down(pyray.KEY_UP):
            dy = 0
        
        if pyray.is_key_down(pyray.KEY_DOWN):
            dy = 0

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction

    def get_coordinate(self,velocity):
        x=0
        y=0
        if pyray.is_key_pressed(pyray.KEY_ENTER):
           
            
            velocity= Point(x,y)
           
        return velocity