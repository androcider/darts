import random

class Dealer:

    def _init_(self):
        pass

    def create_deck(self):
        numbers =['A','2','3','4','5','6','7','8','9','T','J','Q','K']
        suits = ['D','H','S','C']
        deck = []
        for s in suits:
            for n in numbers:
                card = (f'{n}{s}')
                deck.append(card)
        return deck
    def shuffle(self,deck):
        self.shuffled_deck= random.shuffle(deck)
        shuffled_deck=self.shuffled_deck
        return shuffled_deck   
    # def update_score(self,deal,choice):
        
    #     return update_score
    def deal(self,shuffled_deck):
        deal = random.choice(shuffled_deck)
        return deal
    def compare_cards(self,card1,card2,choice):
        card_conversion ={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':1}
        card_number1 = [h[0] for h in card1]
        card_number2 = [h[0] for h in card2]
        card_value1= [card_conversion[i] for i in card_number1[0]] 
        card_value2= [card_conversion[i] for i in card_number2[0]] 
        if card_value1[0] == card_value2[0]:
            print("The values are the same. No points awarded.")
            return 0
        if choice == "h":
            if card_value2[0] > card_value1[0]:
                return 100
            else:
                return -75
        elif choice == "l":
            if card_value1[0] > card_value2[0]:
                return 100
            else:
                return -75
    def update_score(self,score,score_update):
        score += score_update
        return score