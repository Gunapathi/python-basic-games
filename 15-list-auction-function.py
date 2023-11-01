auct_dict = {}


def auction_detail():
    auct_dict[input("Enter your name: ")] = int(input("Enter the bid value: "))

    if input("type Yes to add new ").lower() == 'yes':
        auction_detail()
    else:
        highest_bid = 0
        winner = ""
        for key in auct_dict:
            if auct_dict[key] > highest_bid:
                highest_bid = auct_dict[key]
                winner = key
        print(f"Winner of the bid {winner}")


auction_detail()
