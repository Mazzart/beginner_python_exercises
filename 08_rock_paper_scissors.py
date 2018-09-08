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
    if game == 'yes':
        print("We are starting Rock-Paper-Scissors game.")
        player_1 = input("First player enter your choice: ")
        player_2 = input("Second player enter your choice: ")
        player_3 = input("Third player enter your choice: ")
    else:
        print("OK, see you later.")
        break
