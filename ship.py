from square import Square
from water import Water


class Ship:

    def __init__(self, length):
        """
        Constructs a *Ship* object and creates the number of square objects
        equal to *Ship* object's length.
        Parameters:
        ----------
        length: int

        Raises:
        ------
        TypeError: when length type isn't int
        """
        if not isinstance(length, int):
            raise TypeError

        self.length = length
        self.is_sunk = False
        self.is_hidden = False
        self.square_list = []

        for i in range(length):
            square_i = Square()
            self.square_list.append(square_i)


    def mark_square(self, index):
        """
        Mark a *Square* object in an attribute *ship* by given index.
        Parameters:
        ----------
        index: int

        Raises:
        ------
        TypeError: when index type isn't int
        """
        if not isinstance(index, int):
            raise TypeError

        self.square_list[index].mark()
        self.mark_is_sunk()


    def mark_is_sunk(self):
        """
        Change an *is_sunk* attribute to True if every object which is in an *ship* attribute
        has True is_marked attribute
        Returns:
        -------
        self.is_sunk: bool
        """
        for square in self.square_list:
            if not square.is_marked:
                return self.is_sunk

        self.is_sunk = True
        return self.is_sunk



    def __str__(self):
        """
        Returns all elements of attribute *ship* formatted to string.
        """
        ship_str = ""
        for square in self.square_list:
                ship_str += str(square)
        return ship_str
