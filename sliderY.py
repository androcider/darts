import pyray
from color import Color
from actor import Actor
from point import Point

class Slider(Actor):
    
    def __init__(self, width, height) :
        
        self._width = width
        self._height = height 
        self._text = ""
        self._position = Point(0, 0)
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._velocity = Point(0, 3)
        self._x = 20
        self._y = 20
    def draw_bar (self,x,y):
        
        
        w = self.get_width()
        h = self.get_height()
        x = self.get_x()
        y = self.get_y()
        
        self._color = Color(255,255, 255)
        color = Color(255,255, 255).to_tuple()
        pyray.draw_rectangle(x, y, w, h, color)
        return self.draw_bar

    def draw_slider(self,x,y):
    
        
        w = self.get_width()
        h = self.get_height()
        x = self.get_x()
        y = self.get_y()
        self._color = Color(230, 41, 55)
        color = Color(230, 41, 55).to_tuple()
        pyray.draw_rectangle(x, y, w, h, color)
        
        
        return self.draw_slider  
    
    def get_height(self):
        """Gets the video screen's height.
         
        Returns:
            Grid: The video screen's height.
        """
        return self._height
    def set_velocity(self,velocity):
        
        self._velocity = velocity
        return self._velocity

    def get_width(self):
        """Gets the video screen's width.
        
        Returns:
            Grid: The video screen's width.
        """
        return self._width
    def get_x(self):
        """Gets the video screen's width.
        
        Returns:
            Grid: The video screen's width.
        """
        return self._x
    def get_y(self):
        """Gets the video screen's width.
        
        Returns:
            Grid: The video screen's width.
        """
        return self._y
    def set_x(self,x):
        """Gets the video screen's width.
        
        Returns:
            Grid: The video screen's width.
        """
        self._x = x
        return self._x
    def set_y(self,y):
        """Gets the video screen's width.
        
        Returns:
            Grid: The video screen's width.
        """
        self._y = y
        return self._y
        
    