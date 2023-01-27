import random
import time 
quit = False

while not quit:
    player1 = (input("What do you want to choose, heads[H] or tails[T]: ")).lower()
    player2 = ""
    if player1 == "heads" or player1 == 'h':
        player1 == "heads"
        player2 == "tails"
        print(f"Player 1 choses: {player1}\nPlayer 2 choses: tails")
    elif player1 == "tails" or player1 == "t":
        player1 == "tails"
        player2 == "heads"
        print(f"Player 1 choses: {player1}\nPlayer 2 choses: heads")
    else:
        print("⚠️ Invalid Input!!")
        # quit = True
        break

    print("🪙 Tossing the coin.....")

    toss_result = random.randint(0,1)
    heads_or_tails = ""
    if toss_result == 0:
        heads_or_tails = "tails"
    else:
        heads_or_tails = "heads"

    time.sleep(3)
    
    if player1 == heads_or_tails:
        print(f"It's a {heads_or_tails}")
        print("🥇 Player 1 wins the toss")
    else:
         print(f"It's a {heads_or_tails}")
         print("🥇 Player 2 wins the toss")
         
    toss_coin = (input("Do you want to toss coin [Y] or [N]: ").lower())
    if toss_coin == "n":
        quit = True