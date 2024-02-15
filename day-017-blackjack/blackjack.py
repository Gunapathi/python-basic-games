import random


def deal_card():
    # select one random value and return the value to the given function
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calc_score(cards):
    # take a list of card and return the total score
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # replace 11 with 1 if total > 21 and 11 is also in card
    if 11 in cards and sum(cards) > 21:
        cards.remove(11).append(1)

    return sum(cards)


def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "Lose"
    elif user_score == 0:
        return "Win"
    elif user_score > 21:
        return "You went over, You lose"
    elif comp_score > 21:
        return "Opponent went over, you win"
    elif user_score > comp_score:
        return "You Win"
    else:
        return "You Lose"


def play_game():
    user_cards = []
    comp_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not is_game_over:
        user_total = calc_score(user_cards)
        comp_total = calc_score(comp_cards)
        print(f"Your cards: {user_cards}, your score: {user_total}")
        print(f"Computers first card: {comp_cards[0]}")

        if user_total == 0 or comp_total == 0 or user_total > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while comp_total != 0 and comp_total < 17:
        comp_cards.append(deal_card())
        comp_total = calc_score(comp_cards)

    print(f"Your final hands: {user_cards}, Final Score: {user_total}")
    print(f"Computer final hands: {comp_cards}, Final Score: {comp_total}")
    print(compare(user_total, comp_total))


while input("Do you want to play a game of Blackjack? 'y' or 'n'") == 'y':
    play_game()
