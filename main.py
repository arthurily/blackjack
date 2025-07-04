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

def PlayerHit(deck, playerHand):
    if not deck:
        print("No more cards left in the deck!")
        return True

    newCard = random.choice(deck)
    playerHand.append(newCard)
    deck.remove(newCard)
    playerSum = calculateSum(playerHand)

    print(f"Player's hand: {playerHand} (Total: {playerSum})")

    if playerSum > 21:
        print("Bust! You lose!")
        return True
    return False

def DealerHit(deck, dealerHand):
    while calculateSum(dealerHand) < 17:
        if not deck:
            print("No more cards left in the deck!")
            return True

        newCard = random.choice(deck)
        dealerHand.append(newCard)
        deck.remove(newCard)

    dealerSum = calculateSum(dealerHand)
    print(f"Dealer's hand: {dealerHand} (Total: {dealerSum})")

    if dealerSum > 21:
        print("Dealer busts! You win!")
        return True
    return False

def playOneGame():
    deck = createDeck()
    playerHand = []
    dealerHand = []

    dealCards(deck, playerHand, dealerHand)

    playerSum = calculateSum(playerHand)
    dealerSum = calculateSum(dealerHand)

    print(f"Player's hand: {playerHand} (Total: {playerSum})")
    print(f"Dealer's hand: {dealerHand[0]} and a hidden card")

    # Initial blackjack check
    if playerSum == 21 and dealerSum == 21:
        print("Both you and the dealer have blackjack! It's a tie!")
        return
    elif playerSum == 21:
        print("Player has blackjack! You win!")
        return
    elif dealerSum == 21:
        print("Dealer has blackjack! You lose!")
        return

    # Player turn
    while True:
        action = input("\nDo you want to hit (h) or stand (s)? ").lower()
        if action == 'h':
            if PlayerHit(deck, playerHand):
                return
        elif action == 's':
            if DealerHit(deck, dealerHand):
                return

            playerSum = calculateSum(playerHand)
            dealerSum = calculateSum(dealerHand)

            print(f"\nFinal hands:\n  Player: {playerHand} (Total: {playerSum})\n  Dealer: {dealerHand} (Total: {dealerSum})")

            if playerSum > dealerSum:
                print("\nYou win!")
            elif playerSum < dealerSum:
                print("\nYou lose!")
            else:
                print("\nIt's a tie!")
            return
        else:
            print("\nInvalid input, please enter 'h' or 's'.")


while True:
    playOneGame()
    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break
