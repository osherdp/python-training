from itertools import repeat
import operator


class Matrix:
    """An object representing a matrix data-type."""
    __slots__ = 'matrix'

    def __init__(self, *lines):
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
        if not all([type(line_data) == tuple for line_data in data]):
            return False

        # check if each item in each line is an int.
        if not all([any([isinstance(item, int), isinstance(item, float)]) for
                    line_data in data for item in line_data]):
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

    def _operation_on_matrix(self, other, operation):
        if isinstance(other, Matrix):

            if len(self.tuples) != len(other.tuples):
                raise ValueError("Matrices length don't match")

            matrix_data = [tuple
                           ([operation(self.tuples[i][j], other.tuples[i][j])
                             for j in range(len(self.tuples))]) for i in
                           range(len(self.tuples))]

            if operation == operator.eq:
                return all(
                    [item for line_data in matrix_data for item in line_data])

            elif operation == operator.ne:
                return any(
                    [item for line_data in matrix_data for item in line_data])

            return Matrix(*matrix_data)

        elif isinstance(other, int) or isinstance(other, float):
            return Matrix(
                *[tuple([operation(self.tuples[i][j], other) for j in range(
                    len(self.tuples))]) for i in range(len(self.tuples))])

    def __add__(self, other):
        """Adds two matrices."""
        return self._operation_on_matrix(other, operator.mul)

    def __sub__(self, other):
        return self._operation_on_matrix(other, operator.sub)

    def __mul__(self, other):
        return self._operation_on_matrix(other, operator.mul)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return self._operation_on_matrix(other, operator.truediv)

    def __floordiv__(self, other):
        return self.__truediv__(other)

    def __eq__(self, other):
        return self._operation_on_matrix(other, operator.eq)

    def __ne__(self, other):
        return self._operation_on_matrix(other, operator.ne)

    def __iter__(self):
        return iter(self.tuples)

    def __hash__(self):
        return hash(self.tuples)


m = Matrix.ones(3)
print(m)

m2 = Matrix.unity(3)
print(m2)

print(m + m2)
print(m2 - m)

m = Matrix((1, 2), (3, 4))

print(m * 5)
print(10 * m)

print(m / 2.5)

m2 = Matrix.ones(2)
print(m == m2)
print(m != m2)

for line in m:
    print(line)

dictionary = {Matrix((1, 1), (2, 2)): 2, Matrix((1, 1), (2, 3)): 3}
print(dictionary)
