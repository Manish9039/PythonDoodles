from art import logo

print(logo)
print("Welcome to the secret auction program.")

bid_details = {}
new_bid = True

def find_highest_bid(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = int(bid_details[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while new_bid:
    name = input("What is your name?: ").lower()
    bid = input("What's your bid?: $")
    bid_details[name] = bid

    other_user = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_user == 'no':
        new_bid = False
        find_highest_bid(bid_details)
