import random


def taking_plr_name() -> str:
    """function to take name from player"""
    plr_name : str = ""  # var to hold player name.
    while len(plr_name) < 3 or not plr_name.isalpha():
        plr_name = input("-- Player, enter you name :>> ")
    return plr_name


def taking_lvl(display_name : str) -> int:
    """taking level from player"""
    lvl = 0 # to hold lvl of the game.
    # taking lvl input.
    print("\n")
    print("======================================================")
    print("-- Level are 1, 2, 3, 4, 5 ---------------------------")
    while lvl < 1 or lvl > 5:
        lvl = int(input(f"-- {display_name.upper()}, please Enter your lvl :>> "))
    print("======================================================\n")
    return lvl


def take_a_toss(plr_name : str) -> bool:
    """it's a toss to decide who goes first"""
    faces_list : list = ['0', '1']
    player_choice : str = input("Press 0:HEADS OR 1:TAILS :>> ")
    # checking for player choice.
    if player_choice == faces_list[0]:
        print(f"{plr_name.upper()}, chose HEADS")
    elif player_choice == faces_list[1]:
        print(f"{plr_name.upper()}, chose TAILS")
    else:
        print("INVALID CHOICE")
    return player_choice == random.choice(faces_list)


# game_onn var
game_onn : bool = True

# while loop to run the game.
while game_onn:
    player_name : str = taking_plr_name()  # taking player name.
    taking_lvl(player_name)

    # asking if player want to play again.
    if input("Enter 'a' to play agin :>> ") != 'a':
        game_onn = False