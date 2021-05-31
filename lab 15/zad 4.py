import random


def create_deck():
    for suit in SUITS:
        for pip in PIPS:
            card = (suit,pip)
            deck.append(card)




def deal_deck():
    card = random.choice(deck)
    deck.remove(card)
    return card



CLUB = "\u2663"
HEART = "\u2665"
DIAMOND = "\u2666"
SPADE = "\u2660"

PIPS = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
SUITS = (CLUB, SPADE, DIAMOND, HEART)

deck = []

create_deck()


for i in range(13):
    for j in range(4):
        pip,suit = deal_deck()
        print(suit + pip, end = " ")
    print()