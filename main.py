import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', ]

playerHand = []
dealerHand = []

playerSum = 0
dealerSum = 0

def playRound():
    card1 = random.choice(deck)
    playerHand.append(card1)
    deck.remove(card1)

    card2 = random.choice(deck)
    dealerHand.append(card2)
    deck.remove(card2)

    card3 = random.choice(deck)
    playerHand.append(card3)
    deck.remove(card3)

    card4 = random.choice(deck)
    dealerHand.append(card4)
    deck.remove(card4)

    playerSum = calculateSum(playerHand)
    dealerSum = calculateSum(dealerHand)



def calculateSum(hand):
    total = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            total += 11
            aces += 1
        else:
            total += card

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

dealCard()