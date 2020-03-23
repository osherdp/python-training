from itertools import repeat


class Matrix:
    """An object representing a matrix data-type."""
    __slots__ = 'matrix'

    def __init__(self, *lines: tuple):
        """Constructor.

        lines: a list of tuples containing the data about the matrix.
        """
        if not self._is_valid_data(*lines):
            raise ValueError('Data is not valid')

        super(Matrix, self).__setattr__('matrix', tuple(lines))

    def __setattr__(self, key, value):
        """Defines that Matrix attributes are immutable."""
        raise AttributeError(f'{self.__class__} instance cannot be modified')

    @staticmethod
    def _is_valid_data(*data: tuple) -> bool:
        """Checks if the data given is valid. Valid data is defined if it
        contains tuples of the same length (Matrix only supports n * n) and
        their value is an integer."""
        # check if each line is a tuple.
        if not all([type(line) == tuple for line in data]):
            return False

        # check if each item in each line is an int.
        if not all([type(item) == int for line in data for item in line]):
            return False

        # checks if the given data is of a n * n matrix.
        current_length = len(next(iter(data)))
        if not all([current_length == len(data) for _ in data]):
            return False

        return True

    @classmethod
    def unity(cls, number_lines: int):
        """Generates a matrix with a main diagonal of 1's, everything else
        is 0's.
        """
        tuples_in_chars = [
            list(str('1' + ('0' * i)).zfill(number_lines)[::-1]) for i in
            range(number_lines)]

        return cls(*tuple(
            [tuple(map(int, tuple_chars)) for tuple_chars in tuples_in_chars]))

    @classmethod
    def ones(cls, number_lines):
        """Generates a matrix full of 1's."""
        return cls(*tuple(
            [tuple(repeat(1, number_lines)) for _ in range(number_lines)]))

    def __repr__(self):
        """Returns a string presentation of the matrix instance."""
        return f"({', '.join([str(line) for line in self.matrix])})"

    @property
    def tuples(self):
        """Returns the matrix instance as a tuple of tuples."""
        return self.matrix

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __divmod__(self, other):
        pass


m = Matrix((1, 2), (3, 4))
# m.matrix = ((1, 2), (3, 4))
print(m)
print(m.tuples, type(m.tuples), type(m.tuples[0]))

m = Matrix.unity(4)
print(m)

m = Matrix.ones(3)
print(m)
