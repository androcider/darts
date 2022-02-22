import random



def main():
    class game:
        def _init_(self):
            Dealer.create_deck()
        
    class Player:

        def __init__(self,name,score):
            self.name = name
            self.score=score
    class Dealer:
        def _init_(self,deck):
            self.deal = random.choice(deck)

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
            random.shuffle(deck)
            return deck   



if __name__ == "__main__":
    main()


