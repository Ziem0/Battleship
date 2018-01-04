### Module main
This module contains the logic of game mechanics.

__Methods__

* `show_screen(filename)`
    - parameters: *filename*
    - description: prints out desired screen from *filename* file

* `define_ship_type(ship_types)`
    - parameters: *ship_types*
    - description: asks for ship type input, raises NameError if it's not in *ship_types*

* `define_coordinates()`
    - description: asks for coordinates input and returns them,
                   raises ValueError if they do not fit on board

* `define_ship_turn()`
    - description: asks for ships alignment and returns it, raises NameError if incorrect

* `define_ship_placement(ship_types)`
    - parameters: *ship_types*
    - description: gathers and returns data about placement of a ship on the board

* `show_ship_types(ship_types)`
    - parameters: *ship_types*
    - description: prints out listed available ship types

* `create_player()`
    - description: asks for players name and returns it

* `place_ships_on_board(player)`
    - parameters: *player*
    - description: using data from *define_ship_placement*, inserts ship on *player's* board

* `handle_shooting(shooter, defender)`
    - parameters: *shooter*, *defender*
    - description: asks *shooter* for shot info, processed the shot and it's repercussions

* `print_oceans(shooter)`
    - parameters: *shooter*
    - description: prints out two boards for *shooter* player, one with his ships,
                   one hidden with enemy's ships

* `check_if_win(hit_object, player)`
    - parameters: *hit_object*, *player*
    - description: checks if *player* has any ships left after having one them hit
                   returns bool to declare possible end of game

* `main()`
    - description: prints out initial screens, creates two *Player* objects and their boards,
                   processes players turns until a win condition is met, 
                   prints out end game screen