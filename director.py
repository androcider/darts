def test():
    pass
    while True:

        try:
            choice=input("Higher or Lower? [h/l] " )
            
            if choice == 'h' or  choice == 'l':
                return choice
        except:
            pass
            
        print("That was not a vaild choice! Try again: ")
            
        
choice = test()
print (choice)