import os
from art import logo
print(logo)

def add_new_participants(name, bid):
    new_participants = {
            'name': name,
            'bid': bid
            }
    participants.append(new_participants)

def who_wins(participants):
    max_bid = {'name':"test",
               'bid':0}
    for members in range(1,len(participants)):
        if int(participants[members]['bid']) > int(max_bid['bid']):
            max_bid = participants[members]
    print(f"Congrats {max_bid['name']} wins the bid, {max_bid['name']} has to pay ${max_bid['bid']}")


participants = [{}]
quit = False
while not quit:
    name = input("Enter your name: ")
    bid = input("What's your bid ?: $")

    add_new_participants(name, bid)

    add_more = input("Do you want to add more participants[yes] or [no]: ")
    if add_more == 'no':
        quit = True
    elif add_more =='yes':
        os.system('cls')
who_wins(participants)