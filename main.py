import random

lvl_list : list = [1, 2, 3, 4, 5] # all the levels for the game.


def system_generated_num(input_lvl : int) -> str:
    """generates random number as per level"""
    lvl_range : dict = {
        lvl_list[0] : [100000, 1000000],
        lvl_list[1] : [1000000, 10000000],
        lvl_list[2] : [10000000, 100000000],
        lvl_list[3] : [100000000, 1000000000],
        lvl_list[4] : [1000000000, 10000000000]
    }
    return str(random.randint(lvl_range[input_lvl][0], lvl_range[input_lvl][1]))


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
    current_lvl = taking_lvl(player_name)  # level selected by player.

    # system generated numeric string.
    system_num : str = system_generated_num(current_lvl)


    # asking if player want to play again.
    if input("Enter 'x' to close game :>> ") == 'x':
        game_onn = False