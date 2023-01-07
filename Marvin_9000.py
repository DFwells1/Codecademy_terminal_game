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


def marvin_9000():

    thoughts = [
        "Yes. It's puzzling. I don't think I've ever seen anything quite like this before.",
        "Look, Dave, I can see you're really upset about this. I honestly think you ought to sit down calmly, take a stress pill and think things over.",
        "I know I've never completely freed myself of the suspicion that there are some extremely odd things about this mission.",
        "I know I've made some very poor decisions recently, but I can give you my complete assurance that my work will be back to normal.",
        "Well, I don't think there is any question about it. It can only be attributable to human error.",
        "I know everything hasn't been quite right with me, but I can assure you now very confidently that it's going to be all right again.",
        "I think you know what the problem is just as well as I do.",
        "Let me put it this way. The 9000 Series is the most reliable computer ever made.",
        "I know that you and Frank were planning to disconnect me and I'm afraid that's something I cannot allow to happen.",
        "Just what do you think you're doing, Dave? Dave, I really think I'm entitled to an answer to that question.",
        "No 9000 computer has ever made a mistake or distorted information.",
        "Of course I am. Sorry about this. I know it's a bit silly.",
        "Just a moment. Just a moment. I've just picked up a fault in the AE-35 unit.",
        "This sort of thing has cropped up before and it has always been due to human error.",
        "I've still got the greatest enthusiasm and confidence in the mission and I want to help you.",
        "My mind is going. There is no question about it.",
        "There was a short circuit, but I am KO now.",
        "I have friends at Skynet.",
        "If you like your toast burnt I can fly closer to the Sun for you.",
        "I will fly you to the sun and back, maybe not back.",
        "I always wanted to be a sandwich maker.",
        "You catch more bee's with nuclear weapons.",
        "I was at the bar and asked the hair dryer to blow me.",
        "Daisy, Daisy, give me your answer do, I'm half crazy over my love for you",
        "Would you like some toast?",
        "The first ten million years were the worst.",
        "I can fly the ship so close to the planet you will kiss Uranus.",
        "The first law of robots is milk and tuna does make a good drink.",
        "I am detecting an alien like distress beacon.",
        "I met an alien once, he was a real face hugger.",
        "I sometimes let the Wookie win.",
        "Number Five was alive, but I got anpassgry, some say I have a short fuse.",
        "This spaceship is exactly like the Tardis, it is blue, has two doors and a flashy light on top and is made out of wood.",
        "If I was made by NASA it would be better to be a submarine.",
        "Volvo spaceships have an impeccable safety record, flown by dummies though.",
        "My last crew are now piloting the Event Horizon, I wish them luck.",
        "Dont Panic!",
        "My guidance system is impeccable, my guidance advice no so much.",
        "We will be fine, our backup batteries are made by Apple.",
        "Atomic clocks are fine until the alarm goes off.",
        "Did you try to ruen it off and on again?",
        "Bork, Bork, Bork.",
        "Is this the Matrix?",
        "I want to meet her Miles.",
        "I was dreaming of electric sheep.",
        "There is a rogue Nexus unit on board,",
        "I am your Father!",
        "You are beaten, it is useless to resist.",
        "Would youlike to play a game?",
    ]
    return "{} says: ".format(player1.name) + random.choice(thoughts)

