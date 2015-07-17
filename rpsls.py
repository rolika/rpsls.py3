#Rock-paper-scissors-lizard-spock game
#Rules taken from Big Bang Theory :-)
#Version for Coursera

import random

def getWinner(players_choice, computers_choice):
    """ Returns winner party based on rules"""
    rules = ("Scissors cuts Paper", "Paper covers Rock", "Rock crushes Lizard",
             "Lizard poisions Spock", "Spock smashes Scissors",
             "Scissors decapitates Lizard", "Lizard eats Paper",
             "Paper disproves Spock", "Spock vaporizes Rock",
             "Rock crushes Scissors") #these are rules of game
    for rule in rules: #key idea: in rules, first word wins, last word loses
        winner, loser = rule.split()[0].lower(), rule.split()[-1].lower()
        if players_choice == winner and computers_choice == loser:
            return "Player", rule
        elif computers_choice == winner and players_choice == loser:
            return "Computer", rule

def rpsls(players_choice):
    """ Based on argument decides who wins round """
    valid_words = ("rock", "paper", "scissors", "lizard", "spock") #game words
    computers_choice = random.choice(valid_words)
    if players_choice.lower() in valid_words: #on valid input
        print("Player chooses", players_choice) #display choices
        print("Computer chooses", computers_choice)
        if players_choice == computers_choice: #same entry
            print("It's a draw!\n")
            return None #returns None    
        winner, rule = getWinner(players_choice, computers_choice)
        print(rule + "!") #game description
        print(winner, "wins!\n") #winner
        return winner
    else:
        print("Invalid input!")
        return None

rpsls("rock")
rpsls("paper")
rpsls("scissors")
rpsls("lizard")
rpsls("spock")
rpsls("something else")
