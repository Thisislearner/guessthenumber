import random


def taking_plr_name() -> str:
    """function to take name from player"""
    plr_name : str = ""  # var to hold player name.
    while len(plr_name) < 3 or not plr_name.isalpha():
        plr_name = input("Player, enter you name :>> ")
    return plr_name


# game_onn var
game_onn : bool = True

# while loop to run the game.
while game_onn:

    # asking if player want to play again.
    if input("Enter 'a' to play agin :>> ") != 'a':
        break