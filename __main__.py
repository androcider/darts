import os
from pyexpat.errors import XML_ERROR_INVALID_TOKEN
import random

from actor import Actor
from artifact import Artifact
from cast import Cast
from sliderY import Slider
from director import Director

from keyboard_service import KeyboardService
from video_service import VideoService

from color import Color
from point import Point
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\background.PNG"

FRAME_RATE = 20

MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Darts"
# DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


def main():
    

    # create the cast
    cast = Cast()
    # score = 0
    # # create the banner
    # banner = Actor()
    # banner.set_text(score)
    # banner.set_font_size(FONT_SIZE)
    # banner.set_color(WHITE)
    # banner.set_position(Point(CELL_SIZE, 0))
    # cast.add_actor("banners", banner)

    player1 = Actor()
    player1.set_text("Player1")
    player1.set_position(Point(600,100))
    player1.set_score(501)
    cast.add_actor("players",player1)
    
    player2 = Actor()
    player2.set_text("Player2")
    player2.set_position(Point(730,100))
    player2.set_score(501)
    cast.add_actor("players",player2)

    dart_1 = Actor()
    dart_1.set_text('X')
    dart_1.set_color(WHITE)
    cast.add_actor("player1_darts",dart_1)

    dart_2 = Actor()
    dart_2.set_text('X')
    dart_2.set_color(WHITE)
    dart_2.set_position(Point(25,0))
    cast.add_actor("player1_darts",dart_2)
    
    dart_3 = Actor()
    dart_3.set_text('X')
    dart_3.set_color(WHITE)
    dart_3.set_position(Point(50,0))
    cast.add_actor("player1_darts",dart_3)

    dart_4 = Actor()
    dart_4.set_text('X')
    dart_4.set_color(WHITE)
    dart_4.set_position(Point(75,0))
    cast.add_actor("player2_darts",dart_4)

    dart_5 = Actor()
    dart_5.set_text('X')
    dart_5.set_color(WHITE)
    dart_5.set_position(Point(100,0))
    cast.add_actor("player2_darts",dart_5)
    
    dart_6 = Actor()
    dart_6.set_text('X')
    dart_6.set_color(WHITE)
    dart_6.set_position(Point(125,0))
    cast.add_actor("player2_darts",dart_6)
    
    y_indicator = Slider(20,20)
    x= 20
    y = 50
    y_indicator.set_x = x
    y_indicator.set_y = y
    position = Point(x,y)
    y_indicator.set_position(position)
    cast.add_actor("y_indicator", y_indicator)

    x_indicator = Slider(20,20)
    x= 41
    y = 570
    x_indicator.set_x = x
    x_indicator.set_y = y
    position = Point(x,y)
    x_indicator.set_position(position)
    x_velocity= Point(3,0)
    x_indicator.set_velocity(x_velocity)
    cast.add_actor("x_indicator", x_indicator)
    
    # create the robot
    # x = int(MAX_X / 2)
    # y = int(585)
    # position = Point(x, y)

    # robot = Actor()
    # robot.set_text("#")
    # robot.set_font_size(FONT_SIZE)
    # robot.set_color(WHITE)
    # robot.set_position(position)
    # robot.set_score(0)
    # cast.add_actor("robots", robot)
    

    
    # count = 1
    # for n in range(DEFAULT_ARTIFACTS):
      
        

    #     x = random.randint(1, COLS - 1)
    #     y = 0
    #     position = Point(x,y)
    #     position = position.scale(CELL_SIZE)

    #     r = random.randint(0, 255)
    #     g = random.randint(0, 255)
    #     b = random.randint(0, 255)
    #     color = Color(r, g, b)
        
    #     y2= random.randint(5,15)
    #     velocity = Point(0,y2)
    
        # selector = random.randint(0,1) 
        # if selector == 0:
        #     text = 'G'
        #     gem = Artifact()
        #     gem.set_text(text)
        #     gem.set_font_size(FONT_SIZE)
        #     gem.set_color(color)
        #     gem.set_position(position)
        #     gem.set_score(100)
        #     gem.set_velocity(velocity)
        #     cast.add_actor("artifacts", gem)
        # if selector == 1:
        #     rock = Artifact()
        #     text = 'R'
        #     rock.set_text(text)
        #     rock.set_font_size(FONT_SIZE)
        #     rock.set_color(color)
        #     rock.set_position(position)
        #     rock.set_score(-75)
        #     rock.set_velocity(velocity)
    
        #     cast.add_actor("artifacts", rock)
        # count += 1
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE, DATA_PATH)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":

    main()