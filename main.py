from player import Player
import csv
import os
from colors import Colors


def show_screen(filename):
    """
    Prints screen from a csv file.
    Parameters:
    ----------
    filename: str
    """

    with open(filename, "r") as hello_screen_file:
        hello_screen_reader = csv.reader(hello_screen_file)

        for line in hello_screen_reader:
            print(*line)


def define_ship_type(ship_types):
    """
    Get ship type from a user and returns it.
    Parameters:
    ----------
    ship_types: list

    Returns:
    -------
    user_ship_type: str
    ship_types: list of str

    Raises:
    ------
    NameError: when user's input isn't name of ship type from ship_types list
    """

    user_ship_type = input("\nEnter a ship type: ").title()

    match = 0
    if user_ship_type not in ship_types:
        raise NameError

    return user_ship_type


def define_coordinates():
    """
    Gets coordinates from a user.
    Returns:
    -------
    coordinates: tuple

    Raises:
    ------
    ValueError: when user's input isn't in range from 1 to 10
    """
    user_row_number = int(input("Enter a row number: "))
    user_column_number = int(input("Enter a column number: "))
    coordinates_range = range(10)

    if (user_row_number and user_column_number) not in coordinates_range:
        raise ValueError

    coordinates = (user_column_number, user_row_number)

    return coordinates


def define_ship_turn():
    """Gets a turn of a placement of ship from a user.
    Returns:
    -------
    user_turn: bool

    Raises:
    ------
    NameError: when user's input isn't "y" or "v"
    """
    user_turn = input("Do you want to place the ship horizontally (put 'h')" +
                      " or vertically? (put 'v') ").lower()
    print()

    if user_turn == "h":
        user_turn = True
    elif user_turn == "v":
        user_turn = False
    else:
        raise NameError

    return user_turn


def define_ship_placement(ship_types):
    """
    Gets all information about ship placement.
    Returns:
    -------
    user_ship_type: str
    coordinates: tuple
    user_turn: bool
    """

    show_ship_types(ship_types)
    user_ship_type = define_ship_type(ship_types)
    coordinates = define_coordinates()
    user_turn = define_ship_turn()

    return user_ship_type, coordinates, user_turn


def show_ship_types(ship_types):
    """
    Prints ship types from a ship_types list.
    Parameters:
    ----------
    ship_types: list of str
    """
    print("\nYou can create one of each type of ships: ")
    for key, value in ship_types.items():
        print("{}: {}".format(key, value))


def create_player():
    """
    Asks player for a name, then returns it.
    Returns:
    --------
    Player(name): Player()
    """

    name = input("Enter your name: ")
    return Player(name)


def place_ships_on_board(player):
    """
    Places ships on board on desired coordinates.
    Parameters:
    -----------
    player: Player()
    """

    ship_types = {"Carrier": "five-masted", "Battleship": "four-masted", "Cruiser": "three-masted",
                  "Submarine": "three-masted", "Destroyer": "two-masted"}

    os.system("clear")
    print(player.player_ocean)
    while ship_types:
        try:
            user_ship_type, coordinates, user_turn = define_ship_placement(ship_types)
            player.add_ship_to_ocean(user_ship_type, coordinates, user_turn)
        except NameError:
            print(COLOR.RED + "\nWrong input mate!\n" + COLOR.WHITE)
        except ValueError:
            print(COLOR.RED + "\nCoordinates should be in a range from 1 to 10.\n" + COLOR.WHITE)
        except KeyError:
            print(COLOR.RED + "\nYou can't place ship next to another or out of edge!\n" + COLOR.WHITE)
        else:
            os.system("clear")
            print(player.player_ocean)
            del ship_types[user_ship_type]

    player.player_ocean.add_water()
    os.system("clear")


def handle_shooting(shooter, defender):
    """
    Asks shooter for shot info, processed the shot and it's repercussions,
    Parameters:
    -----------
    shooter: Player()
    defender: Player()

    Returns:
    --------
    win: bool
    True/False: bool
    """

    coordinates = None
    while coordinates is None:

        print("\n" + COLOR.BLUE + COLOR.BOLD + shooter.name + " TURN: " + COLOR.WHITE + COLOR.END)
        print_oceans(shooter)
        try:
            coordinates = define_coordinates()
        except ValueError:
            print(COLOR.RED + "\nCoordinates should be integers in a range from 1 to 10." + COLOR.WHITE)
        else:
            print_oceans(shooter)
            os.system("clear")
            hit_object = shooter.shoot_and_check_if_is_sunk(defender, coordinates)
            if hit_object != "water":
                win = check_if_win(hit_object, defender)
                if win:
                    return win
                coordinates = None

    return False


def print_oceans(shooter):
    """
    Prints out shooter's boards, one visible with his ships, one hidden for enemy.
    """

    print(COLOR.BLUE + "\nYour ocean:" + COLOR.WHITE)
    print(shooter.player_ocean)
    print(COLOR.BLUE + "\nEnemy's ocean:" + COLOR.WHITE)
    print(shooter.enemy_ocean_representation)


def check_if_win(hit_object, player):
    """
    Checks if player has any ships left.
    Parameters:
    -----------
    hit_object: str
    player: Player()

    Returns:
    True/False: bool
    """

    if player.ship_dict[hit_object].is_sunk:
        player.append_sunken_ship(hit_object)
        print(COLOR.RED + "\n" + hit_object + " just sunk!" + COLOR.WHITE)

    if len(player.sunken_ships) == 5:
        return True

    return False


def main():
    """
    Handles game logic.
    """

    show_screen("hello_screen.csv")
    show_screen("instruction_screen.csv")
    player1 = create_player()
    place_ships_on_board(player1)
    player2 = create_player()
    place_ships_on_board(player2)
    show_screen("fight_beginning.csv")
    win = False

    while True:

        player1_win = handle_shooting(player1, player2)

        if player1_win:
            break

        player2_win = handle_shooting(player2, player1)

        if player2_win:
            break

    show_screen("win.csv")


if __name__ == "__main__":
    COLOR = Colors()
    main()
