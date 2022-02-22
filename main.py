
from dealer import Dealer
from player import Player


def main():
    #runs the game

    player = Player()
    dealer = Dealer()
    score = player.get_score()
    deck = dealer.create_deck()
    dealer.shuffle(deck)
    card1 = dealer.deal(deck)
    
 
    while score <=1000:
        print(f"The Card is: {card1}")
        choice=player.get_choice()
        card2 = dealer.deal(deck)
        print(f"Next card was: {card2} ")
        hand_score = dealer.compare_cards(card1,card2,choice)
        score = dealer.update_score(score,hand_score)
        print(f"Your score is: {score}")
        card1 = card2
        if score <= 0 or score >= 1000:
            score += 2000
        else:    
            play_again = player.play_again()
            if play_again == "y":
                score = score
                print("\n")
            else:
                score += 1000

if __name__ == "__main__":
    main()