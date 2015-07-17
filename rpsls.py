#Rock-paper-scissors-lizard-spock game
#Rules taken from Big Bang Theory :-)

import random

def getResult(player, computer, rules):
    """ Assumes valid input from player, which is not equal to computer's. """
    for rule in rules:
        winner, loser = rule.split()[0].lower(), rule.split()[2].lower()
        if player == winner and computer == loser: #on valid and different input
            return 1, 0, rule #either of these conditionals
        elif computer == winner and player == loser: #becomes sooner or later
            return 0, 1, rule #True and returns appropriate result

rules = ("Scissors cuts Paper",
         "Paper covers Rock",
         "Rock crushes Lizard",
         "Lizard poisions Spock",
         "Spock smashes Scissors",
         "Scissors decapitates Lizard",
         "Lizard eats Paper",
         "Paper disproves Spock",
         "Spock vaporizes Rock",
         "Rock crushes Scissors")
players_score, computers_score = 0, 0

valid_words = [rule.split()[0].lower() for rule in rules[:5]]

while True: #main game loop
    computers_choice = random.choice(valid_words)
    players_choice = input("Please enter {}: ".format(", ".join(valid_words))).lower()
    if players_choice in valid_words: #valid input
        print("My choice is:", computers_choice) #computer tells his
        if players_choice == computers_choice: #same entry
            print("We chose the same!") #tells this,
            continue #and begins loop again
        players_mod, computers_mod, message = getResult(players_choice, computers_choice, rules)
        players_score += players_mod
        computers_score += computers_mod
        print(message) #fight description
        print("Player",
              str(players_score) + ":" + str(computers_score),
              "Computer") #displays scores
    elif players_choice in "enough done ok stop quit exit": break #quit game
