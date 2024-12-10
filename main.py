import random

lvl_list : list = [1, 2, 3, 4, 5] # all the levels for the game.


def system_generated_num(input_lvl : int) -> str:
    """generates random number as per level"""
    lvl_range : dict = {
        lvl_list[0] : [100000, 1000000],  # 6 digit num for lvl 1
        lvl_list[1] : [1000000, 10000000],  # 7 digit num for lvl 2
        lvl_list[2] : [10000000, 100000000],  # 8 digit num for lvl 3
        lvl_list[3] : [100000000, 1000000000],  # 9 digit num for lvl 4
        lvl_list[4] : [1000000000, 10000000000]  # 10 digit num for lvl 5
    }
    return str(random.randint(lvl_range[input_lvl][0], lvl_range[input_lvl][1]))


def taking_plr_name() -> str:
    """function to take name from player"""
    plr_name : str = ""  # var to hold player name.
    while len(plr_name) < 3 or not plr_name.isalpha():
        plr_name = input("+-- Player, enter you name :>> ")
    return plr_name


def taking_lvl(display_name : str) -> int:
    """taking level from player"""
    lvl = 0 # to hold lvl of the game.
    # taking lvl input.
    print("\n")
    print("+======================================================+")
    print("+-- Level are 1, 2, 3, 4, 5 ---------------------------+")
    while lvl < 1 or lvl > 5:
        lvl = int(input(f"+-- {display_name.upper()}, please Enter your lvl :>> "))
    print("+======================================================+\n")
    return lvl


def take_a_toss(plr_name : str) -> bool:
    """it's a toss to decide who goes first"""
    faces_list : list = ['0', '1']
    player_choice : str = input("+-- Press 0:HEADS OR 1:TAILS :>> ")
    # checking for player choice.
    if player_choice == faces_list[0]:
        print(f"+-- {plr_name.upper()}, chose HEADS")
    elif player_choice == faces_list[1]:
        print(f"+-- {plr_name.upper()}, chose TAILS")
    else:
        print("+-- INVALID CHOICE --+")
    return player_choice == random.choice(faces_list)


def newline_printer(ttl_newline : int) -> None:
    """prints new lines."""
    for _ in range(ttl_newline):
        print("")  # newline


def digit_place_display(system_gen : str, plr_input : str, display_list : list) -> list:
    """function to created list display for player."""
    plr_display_lst : list = []  # hold match
    # loop to create display.
    for c, a in system_gen, plr_input:
        if c == a:
            pass
        pass
    return plr_display_lst


def taking_player_input(system_gen_len : int):
    """takes input from player"""
    valid_input : str = "" # hold player input.
    # making user player input is valid
    total_chance : int = 3
    while total_chance > 0:
        print(f"+-- {total_chance} of 3 chances left")
        valid_input = input(f"+-- Enter a {system_gen_len} number :>> ")
        # checking for input validity
        if valid_input.isdigit() and len(valid_input) == system_gen_len:
            break
        total_chance -= 1
    return valid_input


# game_onn var
game_onn : bool = True

# while loop to run the game.
while game_onn:
    player_name : str = taking_plr_name()  # taking player name.
    newline_printer(2)  # prints news after taking name.
    current_lvl = taking_lvl(player_name)  # level selected by player.

    # system generated numeric string.
    system_num : str = system_generated_num(current_lvl)
    system_num_len : int = len(system_num)  # length of system generated number.
    newline_printer(3)  # printing newlines.

    # display list for the player.
    display_list_for_player : list = [] # hold digit/dash for player.
    for _ in range(len(system_num)):
        display_list_for_player.append("_")

    print("+===========================================================+")
    print("+-------------- WELCOME TO MATCH THE NUMBER ----------------+")
    print("+===========================================================+")
    newline_printer(2)  # newlines for the game.

    print("+===========================================================+")
    print(f"+-- Hello {player_name.upper()}, you selected {current_lvl} --------")
    print(f"+-- LEVEL : {current_lvl} has generated a {system_num_len} digits number --------")
    print(display_list_for_player)
    newline_printer(2)

    lives_in_game : int = 4  # total lives in the game.
    while lives_in_game >= 0:
        player_input : str = taking_player_input(system_num_len)

        lives_in_game -= 1
    # asking if player want to play again.
    if input("+-- Enter 'x' to close game :>> ") == 'x':
        game_onn = False