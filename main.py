import random


def taking_plr_name() -> str:
    """function to take name from player"""
    plr_name : str = ""  # var to hold player name.
    while len(plr_name) < 3 or not plr_name.isalpha():
        plr_name = input("-- Player, enter you name :>> ")
    return plr_name


def taking_lvl() -> int:
    lvl = 0 # to hold lvl of the game.
    # taking lvl input.
    print("\n")
    print("======================================================")
    print("-- Level are 1, 2, 3, 4, 5 ---------------------------")
    while lvl < 1 or lvl > 5:
        lvl = int(input("-- Please Enter your lvl :>> "))
    print("======================================================\n")
    return lvl


# game_onn var
game_onn : bool = True

# while loop to run the game.
while game_onn:
    player_name : str = taking_plr_name()  # taking player name.

    # asking if player want to play again.
    if input("Enter 'a' to play agin :>> ") != 'a':
        game_onn = False