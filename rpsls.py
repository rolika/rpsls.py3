#Rock-paper-scissors-lizard-spock game
#Rules taken from Big Bang Theory :-)
#Version for Coursera

import random

def rpsls(players_choice):
    """ Returns winner party based on rules"""
    rules = ("Scissors cuts Paper", "Paper covers Rock", "Rock crushes Lizard",
             "Lizard poisions Spock", "Spock smashes Scissors",
             "Scissors decapitates Lizard", "Lizard eats Paper",
             "Paper disproves Spock", "Spock vaporizes Rock",
             "Rock crushes Scissors") #these are rules of game
    valid_words = [rule.split()[0].lower() for rule in rules[:5]]
    computers_choice = random.choice(valid_words)
    if players_choice in valid_words:
        print("\nPlayer chooses:  ", players_choice.capitalize())
        print("Computer chooses:", computers_choice.capitalize())
        if players_choice == computers_choice:
            print("Player and Computer tie!")
            return None
        #key idea: in rules, first word wins, last word loses
        #works only with valid inputs and not-equal choices
        for rule in rules:
            winner, loser = rule.split()[0].lower(), rule.split()[-1].lower()
            if players_choice == winner and computers_choice == loser:
                winner = "Player"
                break
            elif computers_choice == winner and players_choice == loser:
                winner = "Computer"
                break
        print(rule)
        print(winner, "wins!")
        return winner
    print("\nInvalid input!")
    return None

rpsls("rock")
rpsls("paper")
rpsls("scissors")
rpsls("something")
rpsls("lizard")
rpsls("spock")
