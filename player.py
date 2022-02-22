class Player:

    def __init__(self):
        self.score=300

      
       
    def get_choice(self):
       while True:

        try:
            choice=input("Higher or Lower? [h/l] " )
            
            if choice == 'h' or  choice == 'l':
                return choice
        except:
            pass
            
        print("That was not a vaild choice! Try again: ")
            
                
    def get_score(self):

        return self.score
    def play_again(self):
        
      
        while True:

            try:
                    
                play = input("Play again? [y/n]")
                if play == 'y' or  play == 'n':
                    return play
            except:
                pass
                
            print("That was not a vaild choice! Try again: ")