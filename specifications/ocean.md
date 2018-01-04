### Class Ocean
This file contains the logic of Ocean class.

__Attributes__

* `is_hidden`
    - data: bool
    - description: return True if object is hidden

* `coordinates`
    - data: list
    - description: list of tuples made of two integers

* `board`
    - data: dict
    - description: dictionary with coordinates as keys and Water/Ship objects as values

__Instance methods__

* `__init__(self)`

    Construct an *Ocean* object.

* `add_to_ocean(self, coord, item)`

    Add an *item* value with *coord* as key to the *board* attribute.

* `add_water(self)`

    Check *board* attribute for *coordinates* attribute's unused items, add unused items 
    as keys with *Water* objects as values.
