import random

def createDeck():
    return [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4

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

def dealCards(deck, playerHand, dealerHand):
    for i in range(2):
        playerHand.append(deck.pop(deck.index(random.choice(deck))))
        dealerHand.append(deck.pop(deck.index(random.choice(deck))))

def playerHit(deck, playerHand):
    if not deck:
        print("\nno more cards left in the deck!")
        return True

    newCard = random.choice(deck)
    playerHand.append(newCard)
    deck.remove(newCard)
    playerSum = calculateSum(playerHand)

    print(f"player's hand: {playerHand} (total: {playerSum})")

    if playerSum > 21:
        print("\nbust! you lose!")
        return True
    return False

def dealerHit(deck, dealerHand):
    while calculateSum(dealerHand) < 17:
        if not deck:
            print("\nno more cards left in the deck!") #ts is actually impossible btw
            return True

        newCard = random.choice(deck)
        dealerHand.append(newCard)
        deck.remove(newCard)

    dealerSum = calculateSum(dealerHand)
    print(f"dealer's hand: {dealerHand} (total: {dealerSum})")

    if dealerSum > 21:
        print("\ndealer busts! you win!")
        return True
    return False

def playOneGame():
    deck = createDeck()
    playerHand = []
    dealerHand = []

    dealCards(deck, playerHand, dealerHand)

    playerSum = calculateSum(playerHand)
    dealerSum = calculateSum(dealerHand)

    print(f"player's hand: {playerHand} (total: {playerSum})")
    print(f"dealer's hand: {dealerHand[0]} and a hidden card")


    if playerSum == 21 and dealerSum == 21:
        print("\nboth you and the dealer have blackjack! it's a tie!")
        return
    elif playerSum == 21:
        print("\nyou have blackjack! you win!")
        return
    elif dealerSum == 21:
        print("\ndealer has blackjack! You lose!")
        return

  
    while True:
        action = input("\ndo you want to hit (h), stand (s), or ask the bot (?)? ").lower()
        if action == 'h':
            if playerHit(deck, playerHand):
                return
        elif action == 's':
            if dealerHit(deck, dealerHand):
                return
        

            playerSum = calculateSum(playerHand)
            dealerSum = calculateSum(dealerHand)

            print(f"\nfinal hands:\n  you: {playerHand} (total: {playerSum})\n  dealer: {dealerHand} (total: {dealerSum})")

            if playerSum > dealerSum:
                print("\nyou win!")
            elif playerSum < dealerSum:
                print("\nyou lose")
            else:
                print("\nit's a tie!")
            return
        
        elif action == '?':
            suggestedAction = calcStrategy(playerHand, dealerHand)
            print(f"\nbasic strategy suggest you: {suggestedAction}")

        else:
            print("\ninvalid input, please enter 'h' or 's'.")

def calcStrategy(playerHand, dealerHand):
    playerSum = calculateSum(playerHand)
    dealerCard = dealerHand[0]

    if playerSum < 8 and playerSum > 5:
        return 'hit'
    elif playerSum == 9:
        if dealerCard in [3, 4, 5, 6]:
            return 'double'
        else:
            return 'hit'
    elif playerSum == 10:
        if dealerCard in [2, 3, 4, 5, 6, 7, 8, 9]:
            return 'double'
        else:
            return 'hit'
    elif playerSum == 11:
        return 'double'
    elif playerSum == 12:
        if dealerCard in [4, 5, 6]:
            return 'stand'
        else:
            return 'hit'
    elif playerSum in [13, 14, 15, 16]:
        if dealerCard in [2, 3, 4, 5, 6]:
            return 'stand'
        else:
            return 'hit'
    else:
        return 'stand'

        

while True:
    playOneGame()
    again = input("\ndo you want to play again? (y/n): ")
    if again != 'y':
        print("thanks for playing!")
        break
