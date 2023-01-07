import random

class CardDeck:

    def __init__(self):

        self.deck = [
            '2 of Hearts', '2 of Diamonds', '2 of Clubs', '2 of Spades',
            '3 of Hearts', '3 of Diamonds', '3 of Clubs', '3 of Spades',
            '4 of Hearts', '4 of Diamonds', '4 of Clubs', '4 of Spades',
            '5 of Hearts', '5 of Diamonds', '5 of Clubs', '5 of Spades',
            '6 of Hearts', '6 of Diamonds', '6 of Clubs', '6 of Spades',
            '7 of Hearts', '7 of Diamonds', '7 of Clubs', '7 of Spades',
            '8 of Hearts', '8 of Diamonds', '8 of Clubs', '8 of Spades',
            '9 of Hearts', '9 of Diamonds', '9 of Clubs', '9 of Spades',
            'X of Hearts', 'X of Diamonds', 'X of Clubs', 'X of Spades',
            'J of Hearts', 'J of Diamonds', 'J of Clubs', 'J of Spades',
            'Q of Hearts', 'Q of Diamonds', 'Q of Clubs', 'Q of Spades',
            'K of Hearts', 'K of Diamonds', 'K of Clubs', 'K of Spades',
            'A of Hearts', 'A of Diamonds', 'A of Clubs', 'A of Spades',
          ]                         # this table is the format for the deck of cards X is 10 btw
        self.temp = ""              # internal temp variable for deal_from_deck
        self.temp_hands = []        # variable for tracking cards in hands (in play)
        self.used_cards = []        # variable for discarded cards, they can be reshuffled into deck later

    def __repr__(self):             # reports some basic stats about the deck, helps trouble shoot
        return "\nIn deck {}, In hands {}, Used {}".format(len(self.deck), len(self.temp_hands), len(self.used_cards))

    def deck_shuffle(self):     # shuffles the cards - manual call at start - auto call from deck_empty
        random.shuffle(self.deck)
        return

    def deal_from_deck(self):   # check deck empty, fix if empty, deals 1 card from deck into hands - manual call
        if len(self.deck) < 1:
            self.deck_empty()
        temp = self.deck.pop()
        self.temp_hands.append(temp)
        return temp

    def return_hands(self):     # returns played cards from hand back to used cards pile - manual call
        for hand in self.temp_hands:
            self.used_cards.append(hand)
        self.temp_hands = []
        return

    def deck_empty(self):       # moves used cards back to deck, shuffles deck - auto call from deal_from_deck
        print("Deck empty, reshuffling used cards.")
        for used in self.used_cards:
            self.deck.append(used)
        self.used_cards = []
        self.deck_shuffle()
        return


class Player:

    def __init__(self, name="Fred"):

        self.name = name
        self.hand = []
        self.handscore = 0
        self.wins = 0
        self.loss = 0

    def __repr__(self):
        return "\n{} has cards in hand {} with score: {}".format(self.name, self.hand,self.handscore)

    def pstats(self):   # displays players hans and value
        print("\nCards for {}".format(self.name))
        for element in self.hand:
            print(element)
        print("Hand value is : {}".format(self.handscore))

    def sethand(self, cards):
        for i in range(cards):
            self.hand.append(gamedeck.deal_from_deck())

    def handvalue(self):
        cardvalue = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
            "8": 8, "9": 9, "X": 10, "J": 10, "Q": 10, "K": 10, "A": 11
        }
        self.handscore = 0
        for h in self.hand:
            key = h[0]
            self.handscore += cardvalue[key]

    def winner(self):
        print(self.name, "has won this hand!")
        self.wins += 1
        return

    def loser(self):
        print(self.name, "has lost this hand.")
        self.loss +=1
        return

