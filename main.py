import random

cards = ["K", "Q", "J", 9, 8, 7, 6, 5, 4, 3, 2, "A"]

users_cards = []
dealers_cards = []
def Deal_cards(bet):
    for i in range(2):
        users_cards.append(random.choice(cards))
        dealers_cards.append(random.choice(cards))
    print(f"Your bet is ${bet}")
    print(f"Your cards: {users_cards}")
    print(f"Dealer's cards: [{dealers_cards[0]}, X]")

def Check_total(cards):
    total = 0
    if "A" in cards:
        for card in cards:
            if card == "K" or card =="J" or card == "Q":
                total += 10
            elif card == "A":
                total += 11
            total += card
        if total > 21:
            total = 0 
            for card in cards:
            if card == "K" or card =="J" or card == "Q":
                total += 10
            elif card == "A":
                total += 1
            total += card
        return total
    else:
        for card in cards:
            total += card
        return total

def add_card(list):
    list.append(random.choice(cards))
#Ask the user if he wants to play blackjack
start = input("Do you want to play BlackJack. y or n?")
#If yes, then clear the screen and start the game
if start == "y":
    bet = int(input("How much do you want to bet?"))
    Deal_cards(bet)
#ask for the bet amount

continue_game = True
while continue_game:
    hit = input('Do you want another card. y or n?')
    if hit == "y":
        add_card(users_cards)
        Check_total(users_cards)


#Select two random cards for the user and one card for comp
# ask the user if user wants another card or let it pass
#Calculate the 