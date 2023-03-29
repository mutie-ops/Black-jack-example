# creating black jack

# retrievers and random seed not introduced
# try refactoring the code
import random

CARDS = ['A ♦', 'A ♣', 'A ♥', 'A ♠',
         'J ♦', 'J ♣', 'J ♥', 'J ♠',
         'K ♦', 'K ♣', 'K ♥', 'K ♠',
         'Q ♦', 'Q ♣', 'Q ♥', 'Q ♠',
         '1 ♦', '1 ♣', '1 ♥', '1 ♠',
         '2 ♦', '2 ♣', '2 ♥', '2 ♠',
         '3 ♦', '3 ♣', '3 ♥', '3 ♠',
         '4 ♦', '4 ♣', '4 ♥', '4 ♠',
         '5 ♦', '5 ♣', '5 ♥', '5 ♠',
         '6 ♦', '6 ♣', '6 ♥', '6 ♠',
         '7 ♦', '7 ♣', '7 ♥', '7 ♠',
         '8 ♦', '8 ♣', '8 ♥', '8 ♠',
         '9 ♦', '9 ♣', '9 ♥', '9 ♠',
         '10 ♦', '10 ♣', '10 ♥', '10 ♠'
         ]

DEALER_CARDS = []
DEALER_VALUES = []

PLAYER_CARDS = []
PLAYER_VALUES = []

POUCH = [100]


# DEALING FIRST HAND
def player_hand(inp):
    r_card = random.sample(CARDS, k=int(inp))
    for cards in r_card:
        PLAYER_CARDS.append(cards)
    for items in PLAYER_CARDS:
        ti = items.split(" ")[0]
        if ti == 'A':
            PLAYER_VALUES.append(11)
        elif ti == 'Q':
            PLAYER_VALUES.append(10)
        elif ti == 'K':
            PLAYER_VALUES.append(10)
        elif ti == 'J':
            PLAYER_VALUES.append(10)
        elif ti == 'RET':
            PLAYER_VALUES.clear()
            PLAYER_VALUES.append(21)
        else:
            PLAYER_VALUES.append(int(ti))

    print("THE YOUR", PLAYER_CARDS, " values", sum(PLAYER_VALUES))


def dealer_hand(inp):
    r_card = random.sample(CARDS, k=int(inp))
    for cards in r_card:
        DEALER_CARDS.append(cards)
    for items in DEALER_CARDS:
        ti = items.split(" ")[0]
        if ti == 'A':
            DEALER_VALUES.append(11)
        elif ti == 'Q':
            DEALER_VALUES.append(10)
        elif ti == 'K':
            DEALER_VALUES.append(10)
        elif ti == 'J':
            DEALER_VALUES.append(10)
        elif ti == 'RET':
            DEALER_VALUES.clear()
            DEALER_VALUES.append(21)
        else:
            DEALER_VALUES.append(int(ti))
    print("THE DEALER", DEALER_CARDS, " values", sum(DEALER_VALUES))


# DEALING SECOND HAND
def player_deal():
    r_card = random.sample(CARDS, k=int(1))
    for card in r_card:

        ti = card.split(" ")[0]
        if ti == 'A':
            PLAYER_VALUES.append(11)
        elif ti == 'Q':
            PLAYER_VALUES.append(10)
        elif ti == 'K':
            PLAYER_VALUES.append(10)
        elif ti == 'J':
            PLAYER_VALUES.append(10)
        elif ti == 'RET':
            PLAYER_VALUES.clear()
            PLAYER_VALUES.append(21)
        else:
            PLAYER_VALUES.append(int(ti))
        PLAYER_CARDS.append(card)
    print("player deal", PLAYER_VALUES)


def dealer_deal():
    r_card = random.sample(CARDS, k=int(1))
    for card in r_card:
        ti = card.split(" ")[0]
        if ti == 'A':
            DEALER_VALUES.append(11)
        elif ti == 'Q':
            DEALER_VALUES.append(10)
        elif ti == 'K':
            DEALER_VALUES.append(10)
        elif ti == 'J':
            DEALER_VALUES.append(10)
        elif ti == 'RET':
            DEALER_VALUES.clear()
            DEALER_VALUES.append(21)
        else:
            DEALER_VALUES.append(int(ti))
        DEALER_CARDS.append(card)
    print("DEALER deal", DEALER_VALUES)


# Launch game
def game_loop():
    retriever = input('How many retrievers do you want')
    for i in range(int(retriever)):
        CARDS.append("RET 🃏")
    print(CARDS)
    print(f"you have {POUCH} QUATLOOS")
    bet = input("how much QUATLOOS would you like to bet: ")

    for amount in POUCH:
        new_price = int(amount) - int(bet)
        POUCH[0] = new_price
        break

    print(f"you bet {int(bet)} QUATLOOS, you have {POUCH} left ")
    inp = input("how many deck of cards would you like: ")
    player_hand(inp)
    dealer_hand(inp)
    inp2 = input('do you want to deal or not: (Y)/(N): ').lower()
    if inp2 == 'y':
        player_deal()
    elif inp2 == 'n':
        pass
    print(PLAYER_VALUES)
    print("YOUR HAND", PLAYER_CARDS, " values", sum(PLAYER_VALUES))

    'DEALING SECOND HAND OR FAULT FOR DEALER'
    choice = ['DEAL', 'HALT']
    choose = random.choice(choice)

    if choose == 'DEAL':
        dealer_deal()
    print("THE DEALER", DEALER_CARDS, " values", sum(DEALER_VALUES))

    sum_dealer = sum(DEALER_VALUES)
    sum_player = sum(PLAYER_VALUES)

    minimum_p = sum_player - 21
    minimum_d = sum_dealer - 21

    if sum_player > 21 and sum_dealer < 21:
        print("player bust dealer wins")
        print(f"You have {POUCH} left ")

    elif sum_dealer and sum_player == 21:
        print("draw")
        print(f"You have {POUCH} left ")

    elif sum_player == 21:
        print("dealer bust player wins")
        for amount in POUCH:
            new_price = int(amount) + int(bet) * 2
            POUCH[0] = new_price
        print(f"You have {POUCH} left ")

    elif sum_dealer > 21 and sum_player < 21:
        print("dealer bust player wins")
        for amount in POUCH:
            new_prices = int(amount) + int(bet) * 2
            POUCH[0] = new_prices
        print(f"You have {POUCH} left ")

    elif sum_dealer == 21:
        print("player bust dealer wins")
        print(f"You have {POUCH} left ")

    elif sum_player and sum_dealer > 21:
        print("both bust try again")

    elif minimum_p > minimum_d:
        print("dealer bust player wins")
        for amount in POUCH:
            new_price = int(amount) + int(bet) * 2
            POUCH[0] = new_price
        print(f"You have {POUCH} left ")

    elif minimum_d > minimum_p:
        print("player bust dealer wins")
        print(f"You have {POUCH} left ")

    elif sum_dealer == sum_player:
        print("draw")
        print(f"You have {POUCH} left ")


# refactor loop game
while True:
    start = input("press q to start game: ").lower()
    if start == 'q':
        game_loop()
        re_try = input("do you want to play again (y)/(n)").lower()
        if re_try == "y":
            DEALER_CARDS.clear()
            DEALER_VALUES.clear()
            PLAYER_CARDS.clear()
            PLAYER_VALUES.clear()
            game_loop()

            re_try = input("do you want to play again (y)/(n)").lower()

        elif re_try == "n":
            break
        else:
            re_try = input("must be (y)/(n): ").lower()
    else:
        print("must be q")
