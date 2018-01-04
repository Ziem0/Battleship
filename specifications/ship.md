### Class Ship
This file contains the logic of the Ship class.

__Attributes__

* `length`
    - data: int
    - description: amount of *Square* objects

*  `is_sunk`
    - data: bool
    - description: return True wf every of *Square* object's attribute is_marked
                    is True, otherwise return False

*   `is_hidden`
    - data: bool
    - description: return True if object is hidden

*   `ship`
    - data: list
    - description: list of *Square* objects

__Instance methods__

* `__init__(self) `

  Constructs a *Ship* object.

* `mark_square(self, index)`

    Mark a *Square* object in an attribute *ship* by given index.

* `mark_is_sunk(self)`

    Change an *is_sunk* attribute to True if every object in an *ship* attribute
    has True is_marked attribute, otherwise returns None.

* `__str__(self)`

    Returns all elements of attribute *ship* formatted to string.
