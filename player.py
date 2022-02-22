class Player:
    #holds the data for the player
    def __init__(self):
        #creates the player
        self.score=300

      
       
    def get_choice(self):
        #gets the players high or low choice
       while True:

        try:
            choice=input("Higher or Lower? [h/l] " )
            
            if choice == 'h' or  choice == 'l':
                return choice
        except:
            pass
            
        print("That was not a vaild choice! Try again: ")
            
                
    def get_score(self):
        #gets the players score
        return self.score
    def play_again(self):
        #gets the players play again choice
      
        while True:

            try:
                    
                play = input("Play again? [y/n]")
                if play == 'y' or  play == 'n':
                    return play
            except:
                pass
                
            print("That was not a vaild choice! Try again: ")