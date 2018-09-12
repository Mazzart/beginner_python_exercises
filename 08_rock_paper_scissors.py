"""
Make a two-player Rock-Paper-Scissors game. 
Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game.

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

while True:
    game = input("Do you want to play? yes/no: ")
    if game == "yes":
        print("We are starting Rock-Paper-Scissors game.")
        player_1 = input("First player enter your choice: ")
        player_2 = input("Second player enter your choice: ")
        p_1, p_2 = player_1.lower(), player_2.lower()
        if p_1 == p_2:
            print("It is a draw.")
        elif ((p_1 == "rock" and p_2 == "scissors") or
             (p_1 == "scissors" and p_2 == "paper") or
             (p_1 == "paper" and p_2 == "rock")):
            print("Player 1 win.")
        else:
            print("Player 2 win.")
    elif game == "no":
        print("OK, see you later.")
        break
    else:
        print("Invalid input. Try again.")
