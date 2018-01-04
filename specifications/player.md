### Class Player
This file contains the logic of the Player class.

__Attributes__

* `name`
    - data: str
    - description: ship's name

*  `enemy_ocean_representation`
    - data: Ocean
    - description: create instance class Ocean 
                    
*   `player_ocean`
    - data: Ocean
    - description: create instance class Ocean

*   `init_ships_dict`
    - data: dict
    - description: call method init_ships_dict 

*   `sunken_ships`
    - data: list 
    - description: create list

__Instance methods__

* `__init__(self) `

  Constructs a *Player* object.

* `append_sunken_ship(self, hit_object)`
   Parameters:
   	hit_object: str

   Appends hit_object on sunken_ships list.

* `init_ships_dict(self)`

   Creates dictionary: keys - ship's name, values - ship's object
                          

* `add_ship_to_ocean(self, ship_name, coordinates, turn=True)`

   Parameters:
   	ship_name: str
   	coordinates: tuple of integers
   	turn: bool

   Appends ship in specific coordinates and turn to ocean object.

* `check_is_water(self, column, row, ship_length, turn)`

    Parameters:
	column, row, ship_length: int
	turn: bool
    Raises:
	KeyError: when user tries to add ship on another ship or next to.

* `check_range(self, column, row, ship_length, turn)`

   Parameters:
	column, row, ship_length: int
	turn: bool
   Raises:
   	KeyError: when user wants to add ship out of edge

* `shoot_ship(self, enemy, shooted_object)`

   Parameters:
   	enemy: object
   	shooted_object: object
   Returns: key - str

   Checks what kind of object was shooted (square or water)

* `_copy_object(self, object_to_shoot, shoot_coordinates)`

   Parameters:
   	object_to_shoot: object
   	shoot_coordinates: tuple 

   Double representation of player's board

* `shoot_and_check_if_is_sunk(self, enemy, shoot_coordinates)`
   
   Parameters:
   	enemy: object
   	shoot_coordinates: tuple

   Checks what kind of object was shooted and returns its name

