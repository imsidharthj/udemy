from art import logo
# from replit import clear
print(logo)
auction_dictionary = {}
while True:
    name = input("What is your name?:")
    bid = input("What's your bid?: $")
    auction_dictionary[name] = bid
    other_entries = input("type Yes if there is any other user who wants to bid").lower()
    if other_entries == "yes":
        continue
    else:
        break
# def find_highest(inicial_dictionary):
#     highest_bid = None
#     highest_bidder = None
#     for bidder, bid in auction_dictionary.items():
#         if highest_bid is None or bid > highest_bid:
#             highest_bid = bid
#             highest_bidder = bidder
#     return highest_bidder, highest_bid
highest_bid = 0
winner = ""
for bidder in auction_dictionary:
    bid_amount = auction_dictionary[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
print(winner, highest_bid)