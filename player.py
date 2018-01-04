from ocean import Ocean
from ship import Ship
from square import Square
from water import Water


class Player:

    def __init__(self, name):
        """
        Constructs a *Player* object.

        Parameters:
        ----------
        name: str
        enemy_ocean_representation: object
        player_ocean: object
        init_ships_dict: dict
        sunken_ships: list
        ------
        """

        self.name = name
        self.enemy_ocean_representation = Ocean()
        self.player_ocean = Ocean()
        self.init_ships_dict()
        self.sunken_ships = []


    def append_sunken_ship(self, hit_object):
        """
        Appends ship in specific coordinates and turn to ocean object.

        Parameters:
        ----------
        ship_name: str
   	    coordinates: tuple of integers
   	    turn: bool
        ------
        """

        self.sunken_ships.append(hit_object)


    def init_ships_dict(self):
        """
        Creates dictionary: keys - ship's name, values - ship's object.

        Parameters:
        ----------
        """

        self.ship_dict = {}
        self.ship_dict['Carrier'] = Ship(5)
        self.ship_dict['Battleship'] = Ship(4)
        self.ship_dict['Cruiser'] = Ship(3)
        self.ship_dict['Submarine'] = Ship(3)
        self.ship_dict['Destroyer'] = Ship(2)


    def add_ship_to_ocean(self, ship_name, coordinates, turn=True):
        """
        Appends ship in specific coordinates and turn to ocean object.

        Parameters:
        ----------
        ship_name: str
   	    coordinates: tuple of integers
   	    turn: bool
        ------
        """

        if ship_name not in self.ship_dict.keys():
            raise NameError('Invalid ship name')

        ship = self.ship_dict[ship_name]
        ship_lenght = len(ship.square_list)
        column = coordinates[0]
        row = coordinates[1]
        self.check_range(column, row, ship_lenght, turn)
        self.check_is_water(column, row, ship_lenght, turn)

        for value in range(ship_lenght):
            square = ship.square_list[value]
            if turn is True:
                self.player_ocean.add_to_ocean((column+value, row), square)
            elif turn is False:
                self.player_ocean.add_to_ocean((column, row+value), square)


    def check_is_water(self, column, row, ship_lenght, turn):
        """
        Parameters:
        ----------
        column, row, ship_length: int
	    turn: bool

        Raises:
        ------
        KeyError: when user tries to add ship on another ship or next to.
        """

        for x in range(-1, 2):
            for y in range(-1, ship_lenght+1):
                if turn is True:
                    if self.player_ocean.board.get((column+y, row+x)) is not None:
                        raise KeyError
                elif turn is False:
                    if self.player_ocean.board.get((column+x, row+y)) is not None:
                        raise KeyError


    def check_range(self, column, row, ship_lenght, turn):
        """
        Parameters:
        ----------
        column, row, ship_length: int
	    turn: bool

        Raises:
        ------
        KeyError: when user wants to add ship out of edge
        """

        max_value = 10

        if turn is True:
            if column + ship_lenght > max_value:
                raise KeyError
        if turn is False:
            if row + ship_lenght > max_value:

                raise KeyError


    def shoot_ship(self, enemy, shooted_object):
        """
        Checks what kind of object was shooted (square or water).

        Parameters:
        ----------
        enemy: object
   	    shooted_object: object

        Returns: key - str
        ------
        """

        dict_of_ships = enemy.ship_dict
        for key in dict_of_ships:
            item_index = -1
            ship = dict_of_ships[key]
            for square in ship.square_list:
                item_index += 1
                if shooted_object is square:
                    ship.mark_square(item_index)
                    return key


    def _copy_object(self, object_to_shoot, shoot_coordinates):
        """
        Double representation of player's board.

        Parameters:
        ----------
        object_to_shoot: object
   	    shoot_coordinates: tuple
        ------
        """

        self.enemy_ocean_representation.add_to_ocean(shoot_coordinates, object_to_shoot)


    def shoot_and_check_if_is_sunk(self, enemy, shoot_coordinates):
        """
        Checks what kind of object was shooted and returns its name.

        Parameters:
        ----------
        enemy: object
   	    shoot_coordinates: tuple

        ------
        """

        object_to_shoot = enemy.player_ocean.get_item_from_ocean(shoot_coordinates)
        self._copy_object(object_to_shoot, shoot_coordinates)

        if type(object_to_shoot) is Square:
            shooted_object_name = self.shoot_ship(enemy, object_to_shoot)
        elif type(object_to_shoot) is Water:
            object_to_shoot.mark()
            shooted_object_name = 'water'

        return shooted_object_name
