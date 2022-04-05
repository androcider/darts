import random
from PIL import Image
# from __main__ import DATA_PATH 
from point import Point
from sliderY import Slider
from video_service import VideoService
from color import Color
import os
from score import Score
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.count = 0

        self._x = 0
        self._y = 0
        self.dart_count =  0
        self.turn= 'player1'
        self.x_coordinates =[]
        self.y_coordinates = []
        self.dart_scores= {}
       
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """


        # player1_darts = cast.get_actors("player1_darts")
        # for dart in player1_darts:
        x = self._x
        y = self._y
        # robot = cast.get_first_actor("robots")
        # velocity = self._keyboard_service.get_direction()
        # robot.set_velocity(velocity)      
        player1 = cast.get_first_actor("players")
        dart= cast.get_first_actor("player1_darts")

        y_indicator= cast.get_first_actor("y_indicator")
        x_indicator= cast.get_first_actor("x_indicator")
        
        # y_indicator.draw_bar(20,20)
        
        if self.count %2 == 0:
            if y_indicator.get_position().get_y() >= 530:
                position = Point(20,50)
                y_indicator.set_position(position)
            y_indicator_velocity = y_indicator.get_velocity()

            y_velocity= self._keyboard_service.get_coordinate(y_indicator_velocity)
            
            y_indicator.set_velocity(y_velocity)
            if y_indicator.get_velocity().get_y()==0:
                position= y_indicator.get_position()
                y_indicator.set_position(position)

                        
                   
            else:
                y_indicator.move_next(50,550)
            
            self.count +=1

        elif self.count %2 == 1:     
            if x_indicator.get_position().get_x() >= 530:
                position = Point(41,570)
                x_indicator.set_position(position)
            x_indicator_velocity = x_indicator.get_velocity()

            x_velocity= self._keyboard_service.get_coordinate(x_indicator_velocity)
            
            x_indicator.set_velocity(x_velocity)
            if x_indicator.get_velocity().get_x()==0:
                position= x_indicator.get_position()
                x_indicator.set_position(position)
                self._x = x_indicator.get_position().get_x() 
                self._y = y_indicator.get_position().get_y()
                self.x_coordinates.append(self._x)
                self.y_coordinates.append(self._y)
                dart.set_y(self._y)     
                dart.set_x(self._x) 
         
            else:
                x_indicator.move_next(850,20)
            self.count += 1
        

        # print(self.x_coordinates[0])            

        print(self._x)
                
        player2 = cast.get_second_actor("players")
                

            
    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        dart1= cast.get_first_actor("player1_darts")
        background=  os.path.dirname(os.path.abspath(__file__)) + "\\background.PNG"
        image_original = Image.open(background)

        pixels_original = image_original.load()
        player1 = cast.get_first_actor("players")
        player2 = cast.get_second_actor("players")
        y_indicator = cast.get_first_actor("y_indicator")
        x_indicator= cast.get_first_actor("x_indicator")
        # dart1= cast.get_first_actor("player1_darts")
        x = self._x
        y = self._y

        # background=  os.path.dirname(os.path.abspath(__file__)) + "\\background.PNG"
        # image_original = Image.open(background)

        # pixels_original = image_original.load()



 
        # x = random.randint(1, 59) 
        # y = 0
        # position = Point(x,y)
        # position = position.scale(15)
        # banner = cast.get_first_actor("banners")
        # robot = cast.get_first_actor("robots")
        # artifacts = cast.get_actors("artifacts")

        # max_x = self._video_service.get_width()
        # max_y = self._video_service.get_height()
        # robot.move_next(max_x, max_y)
        # if self.dart_count <= 3:    
            # if self.count == 0:
            #     if y_indicator.get_position().get_y() >= 530:
            #         position = Point(20,50)
            #         y_indicator.set_position(position)
            #     y_indicator_velocity = y_indicator.get_velocity()

            #     y_velocity= self._keyboard_service.get_coordinate(y_indicator_velocity)
                
            #     y_indicator.set_velocity(y_velocity)
            #     if y_indicator.get_velocity()==Point(0,0):
            #         position= y_indicator.get_position()
            #         y_indicator.set_position(position)
        
                    
            #     else:
            #         y_indicator.move_next(50,550)
                
            #     self.count +=1

            # elif self.count == 1:     
            #     if x_indicator.get_position().get_x() >= 530:
            #         position = Point(41,570)
            #         x_indicator.set_position(position)
            #     x_indicator_velocity = x_indicator.get_velocity()

            #     x_velocity= self._keyboard_service.get_coordinate(x_indicator_velocity)
                
            #     x_indicator.set_velocity(x_velocity)
            #     if x_indicator.get_velocity()==Point(0,0):
            #         position= x_indicator.get_position()
            #         x_indicator.set_position(position)
                    
                    
            #     else:
            #         x_indicator.move_next(850,20)
            #     self.count -= 1
            
            #     self._y = y_indicator.get_position().get_y()
            #     print(y)
            #     dart.set_y(y)
            #     self._x = x_indicator.get_position().get_x() 
            #     print(x)
            #     dart.set_x(x)
            # x_indicator.get_velocity()==Point(0,0): 

        
        # dart_position = Point(self._x,self._y)
        # dart1.set_position(dart_position)  
        # print(x,y)  
        # # color = Color.get_r_g_b(x,y)
        # r,g,b,a = pixels_original[(x+10),(y+10)]
        # print (f'{r},{g},{b},{a}')
        # key = (r,g,b)
        # print(key)
        # dart1_score = Score()
        # dart1_score = dart1_score.find_score(key)
        # self.dart_scores['dart1'] = dart1_score
        # player1_score = player1.get_score()-dart1_score
        # player1.set_score(player1_score)
        # print(dart1_score)
        # self._video_service._draw_score(600,350, dart1_score)
        # print(dart_score)
        # self.dart_count +=1
        # print(dart.get_position().__dict__)
            # color = Color.get_color(image,self._x,self._y)
        # self._video_service.draw_dart(dart)
        dart_position = Point(self._x,self._y)
        dart1.set_position(dart_position)  
        print(x,y)  
        # color = Color.get_r_g_b(x,y)
        r,g,b,a = pixels_original[(x+10),(y+10)]
        print (f'{r},{g},{b},{a}')
        key = (r,g,b)
        print(key)
        dart1_score = Score()
        dart1_score = dart1_score.find_score(key)
        self.dart_scores['dart1'] = dart1_score
        # new_score=(player1.get_score()-dart1_score)
        # player1.set_score(new_score)
        self._video_service._draw_score(600,200, self.dart_scores['dart1'])
        
        # if y_indicator.get_position().get_y() >= 20:

        #     y_indicator.set_velocity(0,-3)
        #     y_indicator.move_next(20,550)
        #     y = y_indicator.get_position().get_y()
        #     print (y)  
            
        # y_indicator.set_position(position)
        # y= y_indicator.get_y()
        
        # x= y_indicator.get_x()
        # y_indicator.draw_bar(x,y)

            # print (indicator.get_y())

        
        # for artifact in artifacts:
        #     score = robot.get_score()
        #     banner.set_text(f"SCORE: {score} ")
        #     x = random.randint(1, 59)
        #     y = 0
        #     position = Point(x,y)
        #     position = position.scale(15)
        #     artifact.move_next(max_x,max_y)
        #     if robot.get_position().equals(artifact.get_position()):
        #         score += artifact.get_score()
        #         robot.set_score(score)
        #         print(score)
        #         banner.set_text(f"SCORE: {score} ")  
#         artifact.set_position(position)
        #     if Point.get_y(artifact.get_position()) >= max_y:
        #         artifact.set_position(position)

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
       
        self._video_service.get_background()
        self._video_service.clear_buffer()
        player1 = cast.get_first_actor("players")
        player2 = cast.get_second_actor("players")   
        y_slider=cast.get_first_actor("y_indicator")
        x_slider=cast.get_first_actor("x_indicator")
        self._video_service.draw_slider(y_slider)
        self._video_service.draw_slider(x_slider)
    
        
        player1_darts=cast.get_actors("player1_darts")
        # player1_dart.set_text('X')
        player2_darts=cast.get_actors("player2_darts")
        # actors = cast.get_all_actors()
        
        self._video_service.draw_actors(player1_darts)
        self._video_service.draw_actors(player2_darts)
        players=cast.get_actors("players")
        # actors = cast.get_all_actors()
        self._video_service.draw_actors(players)
        player1_score = player1.get_score()
        player2_score = player2.get_score()
        self._video_service._draw_score(600,150,player1_score)
        self._video_service._draw_score(730,150,player2_score)

        

        self._video_service._draw_score
        self._video_service.flush_buffer()